# TradingAgents Analysis

A dated collection of AI-assisted investment research, with source checks and explicit limitations.

Read [how the TradingAgents pipeline works](PIPELINE.md) for the analyst, debate, decision and review stages.

## Reports

See [the report index](reports/README.md). Each report folder contains a readable report, the model's original analysis, reviewed data checks, and run metadata.

## Adding a report

1. Run TradingAgents in your local environment with a new run ID. Keep API keys outside this repository.
2. Review the output against market data and primary sources. A stronger model does not guarantee factual accuracy.
3. Create a Markdown review file explaining verified facts, corrections and remaining uncertainties.
4. Export with the standard-library Python script:

   ```bash
   python3 scripts/import_report.py --state /path/to/full_states_log_DATE.json --review /path/to/review.md --slug ARM-2026-11-12-pro-fred
   ```

5. Inspect the generated files, commit and push. The script does not publish automatically.

Reports are research snapshots, not personalised investment advice. Model ratings are attributed to the model, and no orders are placed. Later reports do not silently replace earlier runs.

Generated using [TradingAgents](https://github.com/TauricResearch/TradingAgents). Source material remains subject to its original terms; citations identify the providers and publishers.
