"""Export a reviewed TradingAgents state into a dated, shareable report folder."""
import argparse
import datetime
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = {
    "final_trade_decision": "Final model decision",
    "market_report": "Technical analysis",
    "fundamentals_report": "Fundamental analysis",
    "news_report": "News and macroeconomic analysis",
    "sentiment_report": "Sentiment analysis",
    "investment_plan": "Research manager conclusion",
    "trader_investment_plan": "Trader proposal",
}
SAFE_SETTINGS = {
    "version", "analysts",
    "llm_provider", "quick_think_llm", "deep_think_llm",
    "quick_think_provider", "deep_think_provider", "max_tokens",
    "max_debate_rounds", "max_risk_discuss_rounds", "output_language",
    "data_vendors", "tool_vendors", "selected_analysts", "asset_type",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--slug", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.slug):
        parser.error("Invalid slug")
    original = json.loads(args.state.read_text())
    review = args.review.read_text()
    clean = {key: original.get(key, "") for key in SECTIONS}
    clean.update({key: original.get(key) for key in ("company_of_interest", "trade_date", "final_rating")})
    clean["run_settings"] = {k: v for k, v in original.get("run_settings", {}).items() if k in SAFE_SETTINGS}
    # Refuse obvious credentials and local user paths before writing shareable files.
    content = json.dumps(clean) + review
    if re.search(r"sk-or-v1-[A-Za-z0-9]+|gh[pousr]_[A-Za-z0-9]+|/home/[^/]+/|api_key=[^\s&]+", content):
        parser.error("Potential credential or private local path in export; review before publishing")
    dest = ROOT / "reports" / args.slug
    dest.mkdir(parents=True, exist_ok=False)
    (dest / "analysis.json").write_text(json.dumps(clean, indent=2, ensure_ascii=False) + "\n")
    (dest / "review.md").write_text(review)
    metadata = {"ticker": clean["company_of_interest"], "analysis_date": clean["trade_date"],
                "framework": "TradingAgents", "framework_url": "https://github.com/TauricResearch/TradingAgents",
                "model_rating": clean["final_rating"], "exported_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "run_settings": clean["run_settings"]}
    (dest / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    title = f"{metadata['ticker']} — {metadata['analysis_date']}"
    parts = ["# " + title, "## Review and source checks", review,
             "## Original model output\n\nThe following sections are preserved as generated. Review notes above take precedence where discrepancies are identified."]
    for key, heading in SECTIONS.items():
        if clean[key]:
            parts.append("## " + heading + "\n\n" + clean[key])
    (dest / "README.md").write_text("\n".join(line.rstrip() for line in "\n\n".join(parts).splitlines()) + "\n")
    rows = ["# Reports", "| Date | Ticker | Model rating | Report |", "|---|---|---|---|"]
    for file in sorted((ROOT / "reports").glob("*/metadata.json"), reverse=True):
        meta = json.loads(file.read_text())
        rows.append(f"| {meta['analysis_date']} | {meta['ticker']} | {meta['model_rating']} | [{file.parent.name}]({file.parent.name}/README.md) |")
    (ROOT / "reports/README.md").write_text("\n\n".join(rows[:1]) + "\n\n" + "\n".join(rows[1:]) + "\n")
    print(dest)


if __name__ == "__main__":
    main()
