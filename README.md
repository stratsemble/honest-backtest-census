# The Honest Backtest Census: How Often Famous Strategies Beat Buy & Hold

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22974115-1682D4.svg)](https://doi.org/10.5281/zenodo.22974115)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-brightgreen.svg)](https://creativecommons.org/licenses/by/4.0/)

**Frozen edition: 2026-09-25.** An openly-licensed, aggregate snapshot of how **25 famous, named trading strategies** performed against **buy & hold** across **36 liquid US stocks & ETFs** over a fixed ~5-year window.

## The headline, failure-framed

Of the **839 strategy-asset backtests that had enough trades to judge** (out of 900 combinations; 61 were too thin and excluded), **about 86% failed to beat simply buying and holding the same asset** over the same window - net of trading costs and slippage, with no look-ahead. Only **~14% (118 of 839)** beat their asset's own buy & hold by any margin.

> **Read the denominator carefully.** It is **strategy-asset backtests**, not "% of strategies." The **~14% beat rate** is the number to anchor on. These are *famous, survivor-selected* names, measured over one fixed period with no out-of-sample split; the figure is a **base rate for this labelled set - not a prediction and not a significance test.**

## What's inside

| file | what it holds |
|---|---|
| `by_asset_class.csv` | beat/fail counts and rate for the **stocks** slice (the headline), plus `crypto` and `all` as context-only rows |
| `by_strategy.csv` | the 25 named strategies on the stocks slice: eligible / beat / lagged counts, beat & fail rate, and a median excess return (a cross-asset central tendency, **not** a forward expectation; `low_sample_flag` marks `n_eligible` < 10) |
| `drawdown_summary.csv` | percentile max-drawdowns, strategy vs buy & hold, per slice |
| `census-2026-09-25.json` | every table above, plus metadata and ready-to-paste citations (APA, BibTeX, attribution) |
| `reproduce.py` | dependency-light script that reloads `by_strategy.csv` and reprints the per-strategy fail rate and the headline |
| `CITATION.cff` | machine-readable citation metadata (powers GitHub's "Cite this repository") |
| `LICENSE.txt` | CC BY 4.0, with the required attribution string |

**Column dictionary (`by_strategy.csv`):** `strategy_slug`, `strategy_name`, `n_eligible`, `n_beat`, `n_lagged`, `n_thin_excluded`, `pct_beat`, `pct_failed`, `median_excess_return`, `low_sample_flag`.

## How it was made

- **Scope:** 25 famous named strategies x 36 liquid US stocks & ETFs = **900 combinations**; **839 judged**, 61 too thin to count.
- **Costs on:** 0.05% per side, next-bar fills, trading costs + slippage applied.
- **No look-ahead:** signals use only closed bars.
- **Benchmark:** **each asset's own buy & hold** (total-return basis) - never a market index.
- **"beat"** = excess return > 0 by any margin; combinations with too few trades/history are flagged **thin** and excluded.
- **One fixed ~5-year window**, canonical parameters over the whole period - **no out-of-sample split, not significance-tested.**
- **Aggregates only:** no per-trade records, no equity curves, no per-combination rows, no strategy parameters, and not the backtesting engine.

**Caveats that travel with every number.** Survivor-selected famous names (labelled, not the whole market). The headline is the **stocks** slice (composition-stable); the `crypto` and `all` rows are **context only** - a small, volatile, survivor-biased sample; an overfitting artifact, not a demonstrated edge.

## Links

- **Project:** https://stratsemble.com
- **Citable permalink (canonical):** https://stratsemble.com/methodology/census/2026-09-25
- **Methodology:** https://stratsemble.com/methodology
- **Concept DOI (all editions):** https://doi.org/10.5281/zenodo.22974115
- **This edition's DOI:** https://doi.org/10.5281/zenodo.22974116

## How to cite

**APA (data set, org-authored):**

> Stratsemble. (2026). *The Honest Backtest Census: How Often Famous Strategies Beat Buy & Hold* (liquid US stocks & ETFs; as of September 25, 2026) [Data set]. https://doi.org/10.5281/zenodo.22974116

**Attribution string (CC BY 4.0):**

> Stratsemble, "The Honest Backtest Census: How Often Famous Strategies Beat Buy & Hold" (Release 2026-09-25), CC BY 4.0, https://stratsemble.com/methodology/census/2026-09-25

**BibTeX:**

```bibtex
@misc{stratsemble_census_20260925,
  author       = {{Stratsemble}},
  title        = {The Honest Backtest Census: How Often Famous Strategies Beat Buy \& Hold},
  year         = {2026},
  note         = {liquid US stocks \& ETFs; as of September 25, 2026, n = 839 judged backtests, 5-year window},
  howpublished = {\url{https://stratsemble.com/methodology/census/2026-09-25}}
}
```

## Licence

Data (c) Stratsemble, released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** licence. You may share and adapt the data, including commercially, provided you give appropriate credit. Full text: https://creativecommons.org/licenses/by/4.0/ - see `LICENSE.txt`.
