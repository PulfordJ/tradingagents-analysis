# ARM — 2026-11-12

## Review and source checks

### Result and review status

**Model rating: Underweight. Model horizon: 3–6 months. Review status: material caveats remain.** The model favours a reduced allocation because of valuation, technical weakness and macro risks, while acknowledging Arm's business strengths. This is the model's conclusion, not an independently endorsed trade recommendation.

The Pro-only rerun improves some earlier inconsistencies, but does not eliminate them. Read these corrections before the original model output:

- The technical table correctly shows price ($199.80) above the 10-day EMA ($196.41), but its later ordering says price is below that EMA. The table's comparison is correct.
- The fundamentals narrative says every quarter's revenue grows sequentially, but its own table falls from approximately $1.49 billion in March to $1.289 billion in June. That narrative is false.
- The report calls the Fed actively hiking. The latest FOMC statement, dated 28 October, **held** the target range at 3.75–4.00%. A rising effective-rate series over earlier months is not proof of a hike at the latest meeting. [Federal Reserve statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm).
- Beta of 3.94 is market-return sensitivity under the estimation method, not proof that total volatility is exactly 3.94 times market volatility. The phrase “zero solvency risk” is also unjustified.
- The forecast of a death cross within 8–14 sessions is a model extrapolation, not a verified event. No completed 50/200 bearish crossover is present in the snapshot.
- Some fundamentals-section moving averages come from a different quote snapshot and differ from the recomputed history below. Use the identified snapshot consistently.

### Scope and provenance

This is an ARM research snapshot for **12 November 2026**, generated with TradingAgents 0.7.1 (upstream commit `9fa1196fffbcfd9de5146d2dd2869df84ab99838`), **DeepSeek V4 Pro in both model roles**, one research/risk debate round, and a 16,384-token response cap. The run used fresh memory and FRED credentials. No portfolio holdings were provided.

**Intraday snapshot:** the run began before the US market closed. Today's daily bar and any indicators using it are provisional. Do not describe them as the final closing price. Separately fetched quote and indicator snapshots may differ while trading continues.

### Price and arithmetic checks

Recomputed directly from the Yahoo Finance OHLC history cached for this run, using rows through 12 November:

| Measure | Recalculated value |
|---|---:|
| Latest daily-bar price (provisional) | $199.80 |
| 20-day simple moving average | $207.39 |
| 50-day simple moving average | $249.19 |
| 200-day simple moving average | $232.41 |

The price is below both the 50-day and 200-day averages. **The 50-day average is above the 200-day average**, not below it. These figures do not establish a completed bearish 50/200 crossover. This corrects a numerical-comparison error in the earlier Flash/Pro run. The check validates arithmetic against the run's cached series, not against an independent exchange feed. [Yahoo Finance ARM history](https://finance.yahoo.com/quote/ARM/history/).

### Primary-source earnings checks

Arm released its September-quarter results on **4 November**, not 5 November. Revenue was $1.443 billion (+27% year over year), with licensing revenue of $773 million and royalties of $670 million. GAAP net income was $130 million and diluted EPS $0.12; non-GAAP diluted EPS was $0.52. These are different accounting measures and must not be mixed.

The year-earlier quarter included a $131 million business-divestiture gain, versus none in the current quarter. Consequently, the decline in GAAP net income alone does not establish deterioration in the underlying operating business. GAAP operating income increased from $163 million to $201 million. [Arm's shareholder letter filed with the SEC](https://www.sec.gov/Archives/edgar/data/1973239/000197323926000141/exhibit992fye27q230-sepx26.htm).

### FRED verification

The FRED key was authenticated successfully. A separate source check pinned both the vintage and observation cutoff to 12 November 2026, rather than using later revisions:

| Series | Latest available observation | Value |
|---|---|---:|
| [Effective federal funds rate — DFF](https://fred.stlouisfed.org/series/DFF) | 9 Nov 2026 | 3.88% |
| [10-year Treasury yield — DGS10](https://fred.stlouisfed.org/series/DGS10) | 9 Nov 2026 | 4.88% |
| [CPI index — CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL) | Oct 2026 | 337.476 |
| [Unemployment rate — UNRATE](https://fred.stlouisfed.org/series/UNRATE) | Oct 2026 | 4.1% |

The CPI figure is an index level, not a percentage inflation rate. Observation dates differ from retrieval dates. Availability of FRED improves macro coverage but does not validate company-specific claims or model conclusions.

### Interpretation limits

The original model sections below are preserved for transparency. Their ratings, targets, stop levels and position sizes are model proposals, not independently validated recommendations or instructions based on the reader's portfolio. Ownership, insider-transaction interpretations, news claims and forecast assumptions require their own checks. No broker orders were submitted.


## Original model output

The following sections are preserved as generated. Review notes above take precedence where discrepancies are identified.

## Final model decision

**Rating**: Underweight

**Executive Summary**: Rate ARM Underweight at $199.80: trim to roughly half to two-thirds of a normal allocation rather than exiting fully. Sell into strength toward $207–$232, keep $163 as the hard invalidation for a further trim or exit on a decisive close below it, and re-engage only if ARM reclaims and holds the 200-day SMA near $232 on rising volume. Do not initiate or add new longs at current levels.

**Investment Thesis**: The bearish trim case prevails, but not to the point of a full Sell. The Conservative Analyst is right that the franchise is structurally strong: 97.5% gross margins, ~$3.25B net cash, ~23% revenue growth, and a genuine data-center royalty inflection argue against exiting and justify retaining a reduced core. However, the Aggressive and Neutral Analysts win the risk/reward debate. At $199.80 the stock still trades near 65x forward EPS with a 3.94 beta and 8% ATR, while the Fed is hiking, the 10-year is near 4.9%, and no 2026 cuts are priced; a high-duration, high-beta asset has more room for multiple compression than expansion. The technical structure is damaged below the 50-day and 200-day SMAs with a death cross approaching, and the bullish stabilization signals (positive MACD histogram, reclaim of the 10 EMA) are early and fragile against an 8% daily ATR. The bounce toward $207–$232 is a trim opportunity, not evidence to hold full size. SoftBank's ~90% distressed ownership and the broad insider selling with zero open-market buys add a real supply and sentiment overhang; the Neutral Analyst's caution that the sales are largely post-vesting is fair, but the absence of any buys is still a yellow flag. The Conservative Analyst's $163 stop is useful, but accepting an ~18% drawdown to test it is too much pain for the current setup. The Neutral Analyst's tiered execution is the soundest synthesis: scale out near $199.80, again near $207 (Bollinger middle), and again near $232 (200 SMA). What would change the call: a decisive close above the 200-day SMA near $232 on rising volume would invalidate the bearish trim thesis and support re-adding; a decisive close below $163 would warrant a further trim or exit; a material forward-multiple repricing lower while data-center royalty momentum remains intact would support rebuilding exposure.

**Price Target**: not provided

**Time Horizon**: 3-6 months

## Technical analysis

# ARM (Arm Holdings plc) — Comprehensive Technical Analysis
## Analysis Date: 2026-11-12 | Exchange: NMS | Sector: Technology / Semiconductors

---

## 1. Executive Summary

ARM is in a **severe medium-to-long-term downtrend** after an extraordinary bubble-like rally and subsequent crash over the past year. The stock peaked at $452.70 on June 18, 2026, and has since collapsed to $199.80 — a **56% drawdown** from the all-time high. However, short-term signals are showing the **first green shoots of stabilization**: price has reclaimed the 10 EMA, the MACD histogram has flipped positive, and RSI is recovering from deeply oversold territory. The overall picture remains bearish, but tactical traders should monitor whether this nascent bounce can extend. A **death cross** (50 SMA crossing below 200 SMA) is approaching rapidly and would structurally confirm the bear market.

---

## 2. Indicator Selection & Rationale

I selected **eight indicators** spanning trend, momentum, volatility, and support/resistance categories — each chosen to minimize redundancy and maximize complementary insight:

| # | Indicator | Category | Rationale |
|---|-----------|----------|-----------|
| 1 | **close_50_sma** | Trend | Medium-term trend direction; dynamic resistance; death-cross monitor |
| 2 | **close_200_sma** | Trend | Long-term trend benchmark; confirms bear market; golden/death cross setups |
| 3 | **close_10_ema** | Trend (short-term) | Responsive momentum gauge; price just reclaimed it — key pivot |
| 4 | **macd** | Momentum | Crossover and divergence analysis; deeply negative but improving |
| 5 | **macdh** | Momentum | Early-warning momentum shift; histogram just turned positive — potential leading signal |
| 6 | **rsi** | Momentum | Overbought/oversold identification; recovering from extreme oversold (27.19) |
| 7 | **boll_lb** | Volatility / Support | Lower Bollinger Band captured the Nov 5 crash low; defines key support floor |
| 8 | **atr** | Volatility / Risk | Extreme volatility (~8% of price); essential for stop-loss placement and position sizing |

**Why not others:** I excluded the Bollinger Middle and Upper bands because the 50 SMA and 10 EMA already serve as dynamic resistance references. I excluded `macds` since MACD and MACDH together capture the signal-line dynamics. I excluded `vwma` because there are no severe volume-spike distortions that demand volume-weighted adjustment beyond what ATR and price structure already capture.

---

## 3. Detailed Indicator Analysis

### 3.1 Trend Structure — Deeply Bearish, Death Cross Imminent

| Moving Average | Current Value | Price Gap | % Above/Below |
|---|---|---|---:|
| **10 EMA** | $196.41 | Price ABOVE by $3.39 | +1.7% |
| **50 SMA** | $249.19 | Price BELOW by $49.39 | –19.8% |
| **200 SMA** | $232.41 | Price BELOW by $32.61 | –14.0% |

**The "waterfall" alignment** (price < 10 EMA < 200 SMA < 50 SMA) is a textbook bearish configuration. However, the 10 EMA reclaimed is noteworthy — the last time price was above the 10 EMA was briefly on November 9–11 as well, after spending virtually all of October and early November below it.

**Death Cross Watch:** The 50 SMA has been declining at an accelerating rate (falling from ~$270 in mid-October to $249.19 today), while the 200 SMA is rising very slowly (from ~$221 to $232.41 over the same period). At current slopes, the 50 SMA will cross below the 200 SMA in approximately **8–14 trading days**. This death cross would be a major structural bearish confirmation if it materializes.

### 3.2 MACD — Deeply Negative but Inflecting

| MACD Component | Value | Direction |
|---|---|---:|
| **MACD Line** | –18.11 | Bottoming / curling up |
| **Signal Line** | –19.01 | Still declining, but slowing |
| **Histogram** | **+0.906** | TURNED POSITIVE (first time since Oct 6) |

The MACD line has been in deeply negative territory since October 13 (when it crossed below zero at approx. –0.51). It troughed around November 5–6 at approximately –22.05, coinciding with the price low of $166.72. Since then, it has been rising — now at –18.11.

**The histogram turning positive on November 12 is the most notable development.** After 26 consecutive trading days of a negative histogram (peaking in negativity at –8.39 on October 16), the flip to +0.91 suggests that downside momentum is exhausting and short-term bullish divergence is emerging. The MACD line is now above its signal line. If this persists, a full MACD bullish crossover (MACD line crossing above zero) would be the next major milestone, though that could take weeks given the current depth.

### 3.3 RSI — Recovering from Oversold, Neutral-Bearish

| RSI | Current | Recent Extremes |
|---|---|---:|
| **RSI (14)** | **43.33** | Oversold: 27.19 (Nov 5) | Overbought zone: >70 not seen since late Sept |

RSI plunged to **27.19 on November 5**, the most oversold reading in the entire dataset. The subsequent bounce to $203.36 (Nov 11) lifted RSI to 44.41, and today's modest pullback to $199.80 brought it to 43.33 — a healthy consolidation of the bounce.

RSI is now in the **neutral zone** (40–45), meaning there is no immediate overbought friction to cap a continued bounce, but also no oversold tailwind. The prior RSI trough at 27.19 is a key reference: if price revisits those levels without making a new RSI low, it would constitute **bullish divergence**.

### 3.4 Bollinger Lower Band — Defining the Crash Floor

| Bollinger Component | Value |
|---|---:|
| **Lower Band** | $167.38 |
| **Middle (20 SMA)** | $207.40 |
| **Upper Band** | $247.41 |

On November 5, the daily low of **$163.13 pierced the lower band ($175.41 at the time)**, and the close at $166.72 was also below the band — a classic "band walk" indicating extreme selling pressure. The lower band has since declined to $167.38 as the 20-day SMA (Bollinger middle) continues to fall.

Today's close at $199.80 is **above the lower band** but still **below the middle band ($207.40)**. The middle band represents the first major resistance in any sustained recovery. A close above the middle band would be a meaningful technical improvement.

### 3.5 ATR — Extreme Volatility Demands Risk Discipline

| ATR | Current Value | As % of Price |
|---|---:|
| **ATR (14)** | **$15.99** | **8.0%** |

The ATR of $15.99 is extraordinarily high in percentage terms. This has been sustained since the September-October crash. For context:
- A 1× ATR daily move is ±$16, or ±8%
- A 2× ATR move is ±$32, or ±16%

Traders should size positions accordingly. A sensible volatility-adjusted stop loss below a swing low (e.g., below the November 5 low of $163.13) would require risk tolerance for moves of $35–$40, which at current volatility is only ~2.2–2.5 ATR. Tight stops will be routinely triggered.

---

## 4. Price Action & Volume Narrative

### The Full Arc: Bubble → Crash → Potential Stabilization

1. **Nov–Dec 2025:** Steady decline from ~$149 to ~$110, losing ~26%. Normal corrective phase.
2. **Jan–early Feb 2026:** Deepening sell-off to a low near $100 (Feb 5 intraday $100.02). **Volume explosion of 24.6M shares on Feb 5** marked capitulation.
3. **Feb–Mar 2026:** Recovery to ~$130–$135 range. Consolidation phase.
4. **Mar 25, 2026:** **Trigger event** — price exploded +30% to $157.07 on 29.6M volume, the highest single-day volume in the dataset.
5. **Apr–mid-June 2026:** Parabolic rally peaking at **$452.70 on June 18** on 34.2M volume. This was a mania-phase move — +188% in less than 3 months from the March breakout.
6. **Late June–July 2026:** Crash. From $453 to $225 by July 29. A 50% drawdown in roughly 30 trading days.
7. **Aug 2026:** Dead-cat bounce to the $280s, followed by renewed selling.
8. **Sept 2026:** Sharp rally from $239 to $333 (Sept 21–22), then equally sharp reversal.
9. **Oct–Nov 2026:** Persistent, grinding decline from $307 to $166.72 (Nov 5). **This leg was -46% in about 5 weeks.**
10. **Nov 5–12, 2026:** Bounce from $166.72 to $203.36, now consolidating at $199.80.

### Key Volume Signals
- **Nov 5, 2026 — 15.4M shares:** Second-highest volume outside the March breakout. This looks like another capitulation event, with price closing at $166.72 after an intraday low of $163.13.
- **Oct 30, 2026 — 10.6M shares:** High-volume breakdown day (close $205.97, open $206.75), suggesting institutional distribution.
- Today's volume (2.64M) is relatively light — consistent with consolidation rather than conviction.

---

## 5. Key Levels to Watch

| Level | Price | Significance |
|---|---|---:|
| **Major Resistance 3** | ~$249 | 50 SMA; approaching death cross point |
| **Major Resistance 2** | ~$232 | 200 SMA; long-term trend-defining level |
| **Intermediate Resistance 1** | ~$207 | Bollinger Middle (20 SMA); first structural resistance |
| **Near-term Pivot** | ~$196 | 10 EMA; bulls defend this for short-term momentum |
| **Current Price** | **$199.80** | — |
| **Near-term Support** | ~$167 | Bollinger Lower Band; tested Nov 5 |
| **Critical Support** | ~$163 | Nov 5, 2026 intraday low — must hold for any bullish thesis |
| **Major Support** | ~$100 | Feb 5, 2026 capitulation low; the "ultimate floor" |

---

## 6. Scenarios & Trade Implications

### Bullish Scenario (Tactical Bounce)
- Price holds above the 10 EMA ($196.41) and pushes through the Bollinger middle ($207.40).
- MACD histogram continues to rise; MACD line curls toward zero.
- RSI climbs above 50.
- **Target:** 200 SMA at ~$232 (a ~16% gain from current). A death cross may still form above price, but the bounce could precede it.
- **Invalidation:** Close below $166.72.

### Bearish Continuation (Base Case)
- The bounce fades at the Bollinger middle ($207) or 200 SMA ($232).
- Death cross forms; institutional selling resumes.
- Price retests $167 (lower band) and potentially breaks below, targeting $150–$163.
- **Invalidation:** Two consecutive closes above the 200 SMA ($232+).

### Neutral / Range-Bound
- Price oscillates between $167 (Bollinger lower) and $207 (Bollinger middle) while moving averages converge toward the death cross.
- This would be a "wait and see" environment best suited for options-based strategies.

---

## 7. Risk Considerations

- **Death cross is a lagging signal** — by the time it triggers, much of the damage is already done. But it could catalyze algorithmic and systematic selling, accelerating downside.
- **ATR at 8%** means that any position held overnight carries genuine gap risk. The average daily range over the past month has been enormous.
- **The post-bubble crash pattern** (June–November) mirrors classic speculative blow-offs in tech/semiconductor names. The speed of the decline from $453 to $167 suggests forced selling, margin calls, or systematic deleveraging rather than orderly revaluation.
- **The $100 level** from February 2026 is a critical macro support. A break below that would open the door to the $70–$80 zone.

---

## 8. Summary Table

| Category | Indicator | Value | Signal | Interpretation |
|---|---|---|---|---:|
| Short-Term Trend | 10 EMA | $196.41 | **Bullish cross** | Price > 10 EMA; short-term momentum improving |
| Medium-Term Trend | 50 SMA | $249.19 | **Bearish** | Price 19.8% below; declining fast |
| Long-Term Trend | 200 SMA | $232.41 | **Bearish** | Price 14% below; death cross approaching |
| Momentum (MACD) | MACD Line | –18.11 | **Bearish, improving** | Deeply negative but curling up from trough |
| Momentum (Early) | MACD Histogram | +0.906 | **Turning Bullish** | First positive reading in 26 days — key inflection |
| Momentum (RSI) | RSI (14) | 43.33 | **Neutral** | Recovering from 27.19 oversold; room to run |
| Support Floor | Bollinger Lower | $167.38 | **Support** | Held on Nov 5; defines bear-market floor |
| Risk / Sizing | ATR (14) | $15.99 (8.0%) | **Extreme volatility** | Position sizing must account for ±$16 daily swings |
| Structural Alert | 50 vs 200 SMA | Gap narrowing | **Death cross ~2 weeks out** | 50 SMA declining at ~$0.70/day toward 200 SMA rising at ~$0.42/day |

---

*All indicator values verified against the deterministic market snapshot for 2026-11-12. Price and volume data sourced from the full one-year OHLCV record. This analysis does not constitute investment advice; traders should combine these technical observations with their own fundamental research and risk tolerance.*

## Fundamental analysis

# ARM Holdings plc (ARM) — Comprehensive Fundamental Analysis

**Report Date: November 12, 2026**

---

## 1. Company Overview

Arm Holdings plc is a British semiconductor and software design company headquartered in Cambridge, UK, trading on the Nasdaq (NMS). Arm does not manufacture chips itself; instead, it licenses its intellectual property (IP) — primarily processor architectures and related technologies — to a vast ecosystem of semiconductor companies, generating revenue through license fees and royalties. Arm's architecture dominates mobile (smartphones, tablets), IoT, automotive, and increasingly cloud/data-center markets. The company's asset-light, royalty-centric model yields structurally high gross margins and strong cash generation.

---

## 2. Market Snapshot & Valuation

| Metric | Value |
|---|---|
| **Market Capitalization** | ~$213.95 billion |
| **TTM P/E Ratio** | **229.83x** |
| **Forward P/E** | 65.03x |
| **PEG Ratio** | 1.68 |
| **Price-to-Book** | 23.54x |
| **TTM EPS** | $0.87 |
| **Forward EPS** | $3.07 |
| **Book Value Per Share** | $8.49 |
| **Dividend Yield** | 0.0% |
| **Beta** | **3.94** |
| **52-Week Range** | $100.02 – $452.70 |
| **50-Day Moving Average** | $249.89 |
| **200-Day Moving Average** | $231.96 |

### Valuation Assessment

Arm trades at an eye-watering TTM P/E of **~230x**, which prices in massive future growth expectations. The forward P/E of 65x and PEG ratio of 1.68 suggest that a substantial portion of earnings growth is already anticipated by the market, though a PEG near 1.7 is not extreme for a high-growth semiconductor IP play. The stock's 3.94 beta makes it roughly **four times as volatile** as the broader market — a high-risk, high-reward profile. The stock, as of this analysis, appears to trade near the lower end of its 52-week range (roughly $198–$200/share), having fallen significantly from its $452.70 high.

---

## 3. Income Statement Analysis

### 3.1 Annual Revenue & Profitability

| Fiscal Year (Mar 31) | Revenue ($M) | YoY Growth | Gross Profit ($M) | Gross Margin | Operating Income ($M) | Net Income ($M) | Diluted EPS |
|---|---|---|---|---|---|---|---|
| **FY2022** | 2,703 | — | 2,572 | 95.2% | 633 | 549 | $0.54 |
| **FY2023** | 2,679 | -0.9% | 2,573 | 96.0% | 671 | 524 | $0.51 |
| **FY2024** | 3,233 | +20.7% | 3,079 | 95.2% | 111 | 306 | $0.29 |
| **FY2025** | 4,007 | +23.9% | 3,886 | 97.0% | 831 | 792 | $0.75 |
| **FY2026** | 4,920 | +22.8% | 4,799 | 97.5% | 900 | 904 | $0.85 |

**Key Takeaways:**
- Revenue growth has **accelerated meaningfully**: from flat in FY2023 to consistent ~23% growth the past two fiscal years.
- **Gross margins are world-class** at 95–97.5%, underscoring Arm's capital-light IP licensing model. Cost of revenue is negligible relative to revenue.
- Net income surged from $306M (FY2024) to $904M (FY2026), nearly tripling in two years.
- EPS more than doubled from $0.29 to $0.85 over the same period.
- FY2024 operating income dipped sharply ($111M vs $671M in FY2023), but this appears to be a one-off — FY2025 and FY2026 rebounded strongly to $831M and $900M respectively.

### 3.2 Quarterly Revenue Trend (Most Recent Quarters)

| Quarter | Revenue ($M) | Gross Profit ($M) | Operating Income ($M) | Net Income ($M) | Diluted EPS |
|---|---|---|---|---|---|
| Q1 FY2026 (Jun 2025) | 1,053 | 1,023 | 114 | 130 | $0.12 |
| Q2 FY2026 (Sep 2025) | 1,135 | 1,106 | 163 | 238 | $0.22 |
| Q3 FY2026 (Dec 2025) | 1,242 | 1,212 | 185 | 223 | $0.21 |
| Q4 FY2026 (Mar 2026)* | ~1,490 | ~1,458 | ~438 | ~313 | ~$0.30 |
| Q1 FY2027 (Jun 2026) | 1,289 | 1,253 | 91 | 270 | $0.25 |
| Q2 FY2027 (Sep 2026) | 1,443 | 1,401 | 201 | 130 | $0.12 |

> *Q4 FY2026 figures derived from annual minus Q1–Q3.

**Quarterly observations:**
- Sequential revenue growth is consistent; every quarter builds on the prior.
- Net income is lumpy quarter-to-quarter (e.g., Q2 FY2027 at $130M vs Q1 FY2027 at $270M). This could reflect timing of license deals, R&D spend, or non-operating items.
- TTM revenue through Sep 2026 stands at **$5.464 billion**.

### 3.3 Profitability & Margin Metrics (TTM)

| Metric | Value |
|---|---|
| Gross Margin | ~97.4% |
| Operating Margin | 17.0% |
| Net Profit Margin | 17.1% |
| EBITDA | $1.128 billion |
| Free Cash Flow | $1.137 billion |
| ROE | 11.3% |
| ROA | 5.5% |

ROE of 11.3% is modest relative to the premium valuation, but it reflects the large cash hoard ($3.25B) that depresses asset efficiency. As earnings scale, ROE should expand meaningfully given the low capital intensity of the business.

---

## 4. Balance Sheet Analysis

### 4.1 Key Balance Sheet Items ($M)

| Period | Total Assets | Cash & Equivalents | Total Liabilities | Current Liabilities | Stockholders' Equity |
|---|---|---|---|---|---|
| Mar 2024 | 7,927 | 1,923 | 2,632 | 1,505 | 5,295 |
| Mar 2025 | 8,932 | 2,085 | 2,093 | 929 | 6,839 |
| Mar 2026 | 10,703 | 2,751 | 2,417 | 1,040 | 8,286 |
| **Sep 2026** | **11,414** | **3,251** | **2,326** | **973** | **9,088** |

### 4.2 Balance Sheet Health Ratios

| Metric | Value | Interpretation |
|---|---|---|
| **Current Ratio** | **6.35** | Extremely strong liquidity |
| **Debt-to-Equity** | **5.5% (0.06x)** | Virtually debt-free |
| **Cash / Total Assets** | 28.5% | Fortress balance sheet |
| **Book Value / Share** | $8.49 | Tangible equity support |

**Balance Sheet Verdict:** Arm's balance sheet is pristine. With $3.25 billion in cash against only $2.33 billion in total liabilities — and minimal long-term debt — the company has zero solvency risk. The current ratio of 6.35 means current assets cover current liabilities over six times. This financial strength provides enormous strategic flexibility for organic investment, M&A, or buybacks.

---

## 5. Cash Flow Analysis

### 5.1 Annual Cash Flows ($M)

| Fiscal Year | Operating CF | Investing CF | Financing CF | CapEx | FCF (Est.) |
|---|---|---|---|---|---|
| FY2022 | 458 | (619) | (32) | 34 | 424 |
| FY2023 | 739 | (138) | (42) | 64 | 675 |
| FY2024 | 1,090 | (516) | (208) | 92 | 998 |
| FY2025 | 397 | (35) | (202) | 219 | 178 |
| **FY2026** | **1,524** | **(325)** | **(548)** | **545** | **979** |

### 5.2 Quarterly Cash Flow (Recent)

| Period | Operating CF | Investing CF | Financing CF | CapEx |
|---|---|---|---|---|
| Q1 FY2027 (Jun 2026) | 902 | (267) | (326) | 197 |
| H1 FY2027 (Sep 2026, 6-mo) | 1,109 | (164) | (439) | 269 |

**Key Observations:**
- FY2025 operating cash flow was anomalously weak at just $397M (vs. $1,090M in FY2024). This appears to have been a working-capital timing issue — FY2026 snapped back powerfully to **$1.524 billion**.
- CapEx is scaling up meaningfully: from $92M (FY2024) to $545M (FY2026), suggesting investment in infrastructure and headcount to capture growth opportunities.
- Free cash flow (TTM) is $1.137 billion, representing a healthy FCF margin of ~20.8%.
- Financing cash flows turned sharply negative (-$548M in FY2026) — likely reflecting share buybacks or debt repayment.
- The first half of FY2027 shows strong OCF of $1.109B (6 months), on pace for another record year.

---

## 6. Insider Transaction Activity (Past 6–12 Months)

This is a critical area for traders. The insider transaction record shows a **pervasive pattern of insider selling** across nearly all top executives and officers:

### Notable Insider Sales

| Date | Insider | Position | Transaction | Approx. Value |
|---|---|---|---|---|
| Sep 21, 2026 | Jason E. Child | CFO | Sale @ $300.00 | $3.12M |
| Aug 27, 2026 | Jason E. Child | CFO | Sale @ $255.33 | $2.66M |
| Jun 2, 2026 | Laura Kathleen Bartels | Officer | Sale @ $392.70 | $4.44M |
| Jun 1, 2026 | William Abbey | Officer | Sale @ $383–416 | $2.64M |
| May 28, 2026 | William Abbey | Officer | Sale @ $343.81 | $1.44M |
| May 21, 2026 | Charlotte Eaton | Officer | Multiple sales | ~$4.2M |
| May 20, 2026 | Jason Child | CFO | Sale @ $226.54 | $7.23M |
| May 20, 2026 | William Abbey | Officer | Sale @ $224–257 | $3.74M |
| May 19, 2026 | Spencer Collins | Officer | Sale @ $215.00 | $8.80M |
| May 18, 2026 | Richard Grisenthwaite | Officer | Sale @ $209.15 | $5.09M |
| May 11, 2026 | Spencer Collins | Officer | Sale @ $208–214 | $11.00M |
| Apr 22, 2026 | Jason Child | CFO | Sale @ $180.00 | $3.83M |
| Mar–Apr 2026 | Rene Haas | CEO | Multiple sales @ $148–163 | ~$11.5M |
| Mar 25, 2026 | Jason Child | CFO | Sale @ $148.37 | $3.16M |

### Insider Awards (Vesting Events)

In **May 2026**, a massive round of stock awards was granted to the executive team, with CEO Rene Haas receiving **265,643 shares**, CFO Jason Child receiving **81,359 shares**, Spencer Collins receiving **69,117 shares**, and other officers receiving substantial grants. This vesting event appears to be the primary driver behind the wave of post-May selling.

### Insider Assessment

- **Direction: Overwhelmingly bearish signal on the surface**, as virtually every insider transaction is a sale. No open-market purchases were recorded.
- **Context matters:** Most sales appear to be systematic post-vesting liquidations following the large May 2026 grant. This is common practice for tech executives managing concentrated equity positions.
- The CEO (Haas) sold at prices between $148–$163 in March/April 2026 — substantially below the 52-week high of $452.70.
- Notably, several officers sold at much higher prices in May–June 2026 ($200–$416 range), suggesting some opportunistic timing.

**Conclusion:** While not a panic signal, the breadth and size of insider selling warrants caution. No insider is "buying the dip," which would be a more constructive signal.

---

## 7. Key Themes & Trader Takeaways

### Bullish Factors
1. **Accelerating revenue growth**: 23% YoY and sequential quarterly gains point to sustained momentum in licensing and royalties.
2. **Extraordinary gross margins** (~97%) and a capital-light model that should expand margins as revenue scales.
3. **Fortress balance sheet**: $3.25B cash, virtually no debt, 6.3x current ratio.
4. **Operating cash flow rebounding**: FY2026 OCF of $1.52B dwarfs FY2025's $397M, suggesting the weak year was transitory.
5. **Secular tailwinds**: AI, edge computing, data-center ARM adoption, and IoT all serve as long-term demand drivers.
6. **PEG of 1.68** — while expensive on P/E, the growth-adjusted valuation is not extreme.

### Bearish / Risk Factors
1. **TTM P/E of 230x** leaves zero room for execution missteps. Any growth slowdown could trigger severe multiple compression.
2. **Beta of 3.94** — the stock is exceptionally volatile; it has already fallen ~56% from its 52-week high.
3. **Heavy insider selling** with zero open-market purchases suggests insiders see current pricing as fair-to-rich.
4. **Lumpy quarterly net income** creates earnings-surprise risk.
5. **Forward P/E of 65x** is still premium-priced even on forward estimates.
6. **CapEx rising fast** ($545M in FY2026 vs $92M in FY2024) — worth monitoring whether this represents productive investment or cost bloat.

---

## 8. Summary Dashboard

| Category | Metric | Value | Signal |
|---|---|---|---|
| **Valuation** | TTM P/E | 229.83x | ⚠️ Very Expensive |
| **Valuation** | Forward P/E | 65.03x | ⚠️ Expensive |
| **Valuation** | PEG | 1.68 | 🟡 Fair-Growth Adjusted |
| **Valuation** | P/B | 23.54x | ⚠️ Premium |
| **Growth** | Revenue Growth (TTM YoY) | ~23% | ✅ Strong |
| **Growth** | Net Income Growth (FY26) | +14% YoY | ✅ Solid |
| **Profitability** | Gross Margin | 97.4% | ✅ World-Class |
| **Profitability** | Net Margin | 17.1% | ✅ Healthy |
| **Profitability** | ROE | 11.3% | 🟡 Moderate |
| **Balance Sheet** | Current Ratio | 6.35 | ✅ Excellent |
| **Balance Sheet** | Debt-to-Equity | 5.5% | ✅ Near-Zero |
| **Balance Sheet** | Cash Position | $3.25B | ✅ Strong |
| **Cash Flow** | TTM FCF | $1.14B | ✅ Robust |
| **Cash Flow** | FCF Margin | 20.8% | ✅ Good |
| **Momentum** | vs. 50-Day MA | Below | 🔴 Weak |
| **Momentum** | vs. 200-Day MA | Below | 🔴 Weak |
| **Momentum** | vs. 52-Week High | -56% | 🔴 Bearish |
| **Insider Activity** | Net Insider Sentiment | Heavy Selling | 🔴 Caution |
| **Risk** | Beta | 3.94 | 🔴 High Volatility |
| **Income** | Dividend Yield | 0.0% | 🟡 None |

---

### Bottom Line

Arm Holdings is a structurally superb business — asset-light, high-margin, strongly growing, and sitting on a pristine balance sheet. However, the stock's valuation (230x TTM P/E) embeds extremely optimistic expectations, and insider selling is pervasive at current levels. Traders should weigh the company's undeniable fundamental strength against the elevated valuation and negative insider sentiment. A pullback toward the lower end of the 52-week range ($100–$150) would present a materially more attractive risk/reward profile, while a break above the 200-day moving average (~$232) could signal renewed momentum. **Cautious on valuation; constructive on the business.**

## News and macroeconomic analysis

# ARM Holdings plc (ARM) — Macro & News Intelligence Report
**Analysis date:** 2026-11-12 | **Sector:** Technology / Semiconductors | **Exchange:** NMS

---

## 1. Executive Summary

ARM is trading in the middle of a three-way squeeze: **(1)** a company-specific post-earnings de-rating on slowing smartphone-royalty growth, **(2)** a sector-wide AI-chip selloff driven by a re-accelerating inflation print and a shock Nvidia CEO exit, and **(3)** a macro regime where the Fed is *hiking* (not cutting), long-end yields are elevated near 4.9%, and high-multiple growth stocks are being repriced.

The stock fell **~13% on Nov 5** despite record revenue (+27% to $1.44B) and an EPS beat, then continued lower — down **~10% on the week** and **roughly a third over the past month**. The fundamental story is bifurcated: data-center royalties doubled (strong) while phone royalties stalled (weak). The single largest structural overhang is the **SoftBank relationship** — the ~90% owner just posted a $7B loss and faces "circular financing" scrutiny.

**Key actionable takeaways:**
- Near-term tape risk remains elevated: no Fed cuts are priced for 2026 (98%), the 10Y sits at ~4.9%, and semis are the epicenter of the selloff.
- The bull case is *structural* (Arm gaining server-CPU share vs. Intel, data-center royalties doubling, global AI capex still robust), but the current valuation likely needs either a macro reprieve (yields/inflation) or a phone-royalty re-acceleration to re-rate.
- **Patient investors should focus on royalty-mix quality (data-center vs. phone) and any sign the SoftBank financing overhang clears** — both flagged by sell-side as gating factors for a re-entry.

---

## 2. Company-Specific News & Catalysts

### 2.1 Earnings: A "good numbers, bad reaction" event
- ARM reported **Nov 5** results: revenue **+27% YoY to a record $1.44B**, adjusted EPS **beat** estimates.
- Despite the beat, the stock **dropped ~13%** the same day. The market's problem: **royalty revenue growth slowed** and **smartphone demand weakened**. Barchart and TIKR both flagged that **"pricier memory stalled Arm's phone royalties,"** while **data-center royalties doubled**.
- The divergence matters: ARM's royalty stream is shifting toward AI/data-center (high growth) away from phones (mature, price-sensitive), but the phone segment is still large enough to drag the blended growth rate.

### 2.2 SoftBank overhang — the "number that matters"
- **SoftBank Group posted its first net loss in nearly two years: ¥1.12 trillion (~$7B)**, driven by a **$3.7B writedown on a US data-center project** amid rising AI-sustainability fears.
- TIKR/others flagged **"circular financing concerns"** — the perception that SoftBank (ARM's ~90% owner) is using its ARM stake as collateral/financing fuel for its own AI bets. This creates a **potential supply/pledging overhang** on the shares and an indirect valuation discount.
- This is the most idiosyncratic ARM-specific risk: even if ARM's fundamentals hold, SoftBank's balance-sheet stress can pressure the stock.

### 2.3 Structural positives still intact
- **UBS:** server CPU demand stayed strong in Q3, with **Arm-based chips and AMD taking share from Intel** — a durable secular tailwind.
- **CoreWeave raised its 2026 revenue outlook**, reviving the AI-chip trade broadly (AMD +4%); supportive for AI infrastructure demand that feeds ARM's data-center royalties.
- **CEO Rene Haas** publicly warned that US resistance to AI data centers (voters rejected ~40 of 41 local ballot measures) could push build-out abroad — **Google committed $15B to Malaysia** for data-center campuses. Implication: global AI capex remains strong *even if* US siting slows; ARM's royalty model is geographically diversified.

### 2.4 Sentiment among professionals
- **Liontrust's "Global Innovation Fund"** disclosed it **bought ARM back after the sharp sell-off** (Q3 2026 letter) — evidence of institutional dip-buying.
- **Barchart** countered: *"Don't chase the Arm stock dip yet"* — arguing patient investors should wait for confirmation (royalty re-acceleration, SoftBank clarity) before buying.
- Mixed sell-side: some price-target cuts amid the broader chip downgrade wave.

---

## 3. Sector Context: The AI-Chip Trade Under Stress

- **Chip stocks suffered their worst day in 19 months last Thursday (Nov 5):** Nasdaq **-5.52%**, S&P 500 **-4.36%** (~$3T erased) — the biggest one-day drops since the April 2025 tariff shock.
- **Nvidia is at its most extreme selling level since 2019**; the chip slide has approached **$5 trillion** in cumulative market-cap loss.
- **Catalyst of the week:** **Jensen Huang is out as Nvidia CEO** (Colette Kress named interim CEO). This is a genuine sector sentiment shock — ARM has heavy correlation to the AI-complex trade even though its business model (licensing/royalties) differs from Nvidia's accelerators.
- **Prediction-market read on Nvidia succession:** Ian Buck **38%** favorite for permanent CEO, Colette Kress **18%**, Tim Cook **6%**; **30%** odds a permanent CEO is named by Dec 31, 2026. Expect ongoing headline risk until resolved.
- **Bargain-hunting has begun:** chip stocks rallied Wednesday (bargain hunting) and **tech rose on CoreWeave results** — suggesting the selling is not uniformly capitulatory; there is two-way flow.

---

## 4. Macro Backdrop — Grounded in FRED Data

The macro environment is a **headwind for high-multiple, long-duration semi stocks**, and critically, it is *different* from the "Fed cutting" narrative that supported growth stocks earlier in the cycle.

| Indicator | Latest | Trend / Signal |
|---|---|---|
| **Fed Funds (effective)** | **3.88%** (Oct) | **Rising:** 3.63 → 3.75 → 3.88 over Aug–Oct. The Fed is *hiking*, not cutting. |
| **10Y Treasury** | **4.88%** (Nov 9) | Elevated; spiked to ~**5.3%** in early Oct, now ~4.84–4.95. High real rates compress growth-stock multiples. |
| **CPI (headline)** | 337.48 (Oct) | **+1.0% in two months** (Aug→Oct) — inflation re-accelerating; a "hot" CPI print was a cited selloff trigger. |
| **Core PCE** | 130.90 (Sep) | Rising steadily (+0.58% over two months) — sticky core inflation. |
| **Unemployment** | **4.1%** (Oct) | Stable (4.1–4.2 range); labor market not yet the Fed's problem. |
| **Yield curve (10Y–2Y)** | **+0.25%** | Positive (not inverted) but **flattening** from +0.51 in early Oct. |
| **VIX** | **17.5** (Nov 11) | Spiked to **28.2 on Nov 5** (selloff day), now normalized. Volatility has *cooled* despite the news flow. |

**Interpretation for ARM:**
- **Hot inflation + a hiking Fed + ~4.9% 10Y yields** = exactly the environment that punishes a stock like ARM, which trades on premium growth multiples (forward earnings discounted at higher rates).
- The VIX normalization (~17.5) suggests **acute panic has passed**, but the macro *level* (high rates) remains a structural drag — this favors a trading range over a V-shaped recovery.
- **Prediction markets** confirm the hawkish tilt: **"No Fed rate cuts in 2026" is priced at 98%** — the market no longer expects accommodation. Meanwhile, **US recession odds are only 2%** — so this is a *"hotter-for-longer"* scenario, not a recession/cut scenario.

---

## 5. Trading Considerations & Actionable Insights

1. **Near-term: expect elevated two-way volatility.** VIX has normalized, but unresolved Nvidia succession (headline risk), hot-inflation data cadence, and the SoftBank overhang argue against chasing bounces without confirmation.

2. **Watch the royalty mix, not just the headline beat.** Data-center royalties doubling is the durable growth engine; phone royalty stalling (memory-price-driven) is the near-term drag. A signal that phone royalties stabilize or data-center share accelerates would be the cleanest fundamental re-entry trigger (Barchart's "be patient" thesis).

3. **SoftBank is the idiosyncratic risk.** The $7B loss and circular-financing concerns are the "number that matters" per TIKR. Any news on SoftBank monetizing/de-risking its ARM stake, or on its data-center writedowns, will move ARM more than typical fundamental news. Monitor SoftBank headlines as a leading indicator for ARM.

4. **Macro gating factor = the 10Y yield.** With no cuts priced for 2026 (98%) and yields near 4.9% after a 5.3% peak, ARM's multiple recovery is likely capped until either inflation cools or yields fall. Long-duration growth longs should respect this; a break of the recent 10Y range (~4.84%) would be constructive, a re-test of ~5% would renew pressure.

5. **Sector beta dominates short-term direction.** ARM's week (-10%) tracked the AI-complex selloff more than its own fundamentals. Nvidia succession resolution (Ian Buck 38% favorite) and CoreWeave-type demand datapoints will drive the group — and ARM's correlation — more than ARM-specific news in the near term.

6. **Institutional dip-buying exists** (Liontrust) but is not yet a consensus; the mixed price-target cuts suggest further downside capitulation is possible before a durable bottom.

---

## 6. Key Points Summary Table

| Category | Factor | Detail | Direction for ARM |
|---|---|---|---|
| **Earnings** | Nov 5 results | Rev +27% to record $1.44B, EPS beat — but stock -13% | ⚠️ Mixed (fundamentals ok, reaction negative) |
| **Royalty mix** | Phone vs. data center | Phone royalties stalled (memory-price drag); data-center royalties **doubled** | 🔺 Long-term positive / 🔻 near-term drag |
| **SoftBank** | $7B loss + circular financing | First loss in ~2 years; $3.7B data-center writedown; stake overhang | 🔻 Negative overhang |
| **Server CPU** | UBS note | Arm + AMD gaining share vs. Intel; demand strong | 🔺 Positive |
| **AI capex** | CoreWeave + Google | CoreWeave raised FY26; Google $15B Malaysia data centers | 🔺 Positive |
| **Sector shock** | Nvidia CEO exit | Huang out; Kress interim; Ian Buck 38% for permanent | ⚠️ Negative sentiment/headline risk |
| **Selloff scale** | Nov 5 rout | Nasdaq -5.52%, S&P -4.36%, ~$3T erased; ~$5T chip slide | 🔻 Negative tape |
| **Fed policy** | Fed funds 3.88% | Rising (3.63→3.88); **hiking, not cutting** | 🔻 Negative (higher discount rates) |
| **Rates outlook** | Polymarket | "No Fed cuts in 2026" = **98%** | 🔻 Negative for growth multiples |
| **10Y yield** | 4.88% | Peaked ~5.3% early Oct; still elevated | 🔻 Negative |
| **Inflation** | CPI / Core PCE | Headline re-accelerating (+1.0%/2mo); core sticky | 🔻 Negative (hot CPI triggered selling) |
| **Recession** | Polymarket | US recession by end-2026 = **2%** | 🔺 Positive (no hard landing priced) |
| **Labor** | Unemployment 4.1% | Stable | 🟡 Neutral |
| **Volatility** | VIX 17.5 | Spiked to 28.2 on Nov 5, now normalized | 🟡 Neutral (panic faded) |
| **Institutional flows** | Liontrust fund | Bought ARM back after sell-off | 🔺 Positive signal |

**Net assessment:** ARM's *secular* story (AI-driven data-center royalty growth, server share gains) remains intact, but the *cyclical* setup is hostile — a hiking Fed, ~4.9% yields, re-accelerating inflation, a SoftBank balance-sheet overhang, and unresolved sector leadership (Nvidia). Expect a volatile trading range with a downward bias until either (a) the 10Y yield rolls over meaningfully, (b) phone-royalty growth stabilizes, or (c) the SoftBank financing overhang clears.

## Research manager conclusion

**Recommendation**: Underweight

**Rationale**: The bull correctly identifies a structurally strong business: ARM reported record revenue of $1.44B (+27% YoY), roughly $4.92B FY2026 revenue (+22.8%), 97.5% gross margins, ~$3.25B net cash, minimal debt, and a genuine data-center royalty inflection with server CPU share gains. Those facts argue against a Sell and justify retaining a reduced core position. But the bear wins the risk/reward debate at $199.80. The stock still trades near 65x forward EPS in a higher-for-longer macro setup with the Fed hiking, the 10-year near 4.9%, and no 2026 cuts priced; a high-beta (3.94) long-duration asset has more room for multiple compression than expansion. The technical structure remains damaged below the 50-day and 200-day SMAs with a death cross approaching; the bull's own stabilization signals are early and fragile. The bull's base case of $232-$249 versus a $163 invalidation offers roughly symmetric-to-unfavorable entry risk, not clear asymmetry. SoftBank's ~90% distressed ownership and the broad insider selling with zero open-market buys create real supply and sentiment overhang. This is not a broken franchise, but it is not yet a place to add or rebuild.

**Strategic Actions**: Trim ARM to an underweight size relative to a standard allocation; target roughly half to two-thirds of normal weight rather than exiting fully. Do not initiate or add new longs at current levels. On the remaining core position, use $163 as the hard invalidation level: a decisive close below it warrants a further trim or exit. Consider using strength toward $207-$232 to reduce exposure or overwrite with covered calls. Re-engage on the long side only if ARM reclaims and holds the 200-day SMA near $232 on rising volume, or if the forward multiple reprices materially lower while data-center royalty momentum remains intact. If already underweight or flat, stay patient and keep ARM on a watchlist rather than chasing stabilization signals.

## Trader proposal

**Action**: Sell

**Reasoning**: The plan maps Underweight to a Sell (trim), and the technical structure supports reducing exposure: ARM trades 14–20% below its 50-day and 200-day SMAs with a death cross roughly 2 weeks out, while the bullish stabilization signals (positive MACD histogram, reclaim of the 10 EMA) are early and fragile against an 8% ATR. I would trim into current levels or strength toward $207–$232 rather than fully exit, since the franchise fundamentals (97.5% gross margin, net cash, data-center royalty inflection) justify keeping a reduced core. For the remaining core, a decisive close below $163 is the hard invalidation; the bearish-trim thesis is invalidated above the 200 SMA.

**Entry Price**: 199.8

**Stop Loss**: 232.41

**Position Sizing**: Reduce to underweight: target roughly half to two-thirds of normal allocation size (do not exit the full position).

FINAL TRANSACTION PROPOSAL: **SELL**
