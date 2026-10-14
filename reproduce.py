#!/usr/bin/env python3
"""
reproduce.py - The Honest Backtest Census (frozen edition 2026-09-25)

Reloads by_strategy.csv and reprints the per-strategy fail rate and the
failure-framed headline, so anyone can verify the published aggregates from
the raw CSV. Pure standard library; no install needed.

HONESTY / CAVEATS (read before quoting any number):
  * Failure-framed. The denominator is strategy-ASSET BACKTESTS (combinations),
    never "% of strategies". Anchor on the ~14% beat rate.
  * Survivor-selected, FAMOUS NAMES - not the whole market. Aggregate rates
    only (no per-trade records). One fixed ~5-year window, no out-of-sample
    split, NOT significance-tested. "beat" = excess return over the asset's own
    buy & hold > 0 by any margin; trading costs + slippage on; no look-ahead.
  * This is a base rate for this labelled set, NOT a prediction.

Run:  python reproduce.py
Optional bar chart (needs matplotlib):  python reproduce.py --plot
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "by_strategy.csv")


def load(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    rows = load(CSV_PATH)

    # Recompute the headline straight from the per-strategy rows (stocks slice).
    total_eligible = sum(int(r["n_eligible"]) for r in rows)
    total_beat = sum(int(r["n_beat"]) for r in rows)
    pct_beat = 100.0 * total_beat / total_eligible if total_eligible else 0.0
    pct_failed = 100.0 - pct_beat

    print("The Honest Backtest Census - frozen edition 2026-09-25")
    print("Stratsemble - CC BY 4.0 - https://stratsemble.com/methodology/census/2026-09-25")
    print("-" * 72)
    print("FAILURE-FRAMED HEADLINE (stocks slice):")
    print(f"  {total_beat} of {total_eligible} judged strategy-asset backtests beat")
    print(f"  the asset's own buy & hold  =  {pct_beat:.0f}% beat  /  {pct_failed:.0f}% FAILED.")
    print("  Denominator = strategy-asset BACKTESTS, not '% of strategies'. Anchor: ~14% beat.")
    print("-" * 72)

    # Per-strategy fail rate, worst first. Rows with 0 eligible trades are
    # listed separately as excluded (too thin to judge) - never as "0% failed".
    judged = [r for r in rows if int(r["n_eligible"]) > 0]
    judged.sort(key=lambda r: (int(r["pct_failed"]), int(r["n_eligible"])), reverse=True)

    print(f"{'strategy':28} {'n':>3} {'beat':>4} {'fail%':>6}  flag")
    for r in judged:
        flag = "low-n" if r["low_sample_flag"].strip().lower() == "true" else ""
        print(f"{r['strategy_name'][:28]:28} {r['n_eligible']:>3} "
              f"{r['n_beat']:>4} {r['pct_failed']:>5}%  {flag}")

    for r in [r for r in rows if int(r["n_eligible"]) == 0]:
        print(f"{r['strategy_name'][:28]:28}   -    -      -   excluded (too thin to judge)")

    print("-" * 72)
    print("NOTE: survivor-selected famous names; aggregate rates only; one fixed")
    print("~5-year window; not significance-tested. A base rate, not a prediction.")

    if "--plot" in sys.argv:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except Exception as exc:  # noqa: BLE001
            print(f"\n[plot skipped: matplotlib not available - {exc}]")
            return
        names = [r["strategy_name"] for r in judged][::-1]
        fails = [int(r["pct_failed"]) for r in judged][::-1]
        fig, ax = plt.subplots(figsize=(8, 9))
        ax.barh(names, fails)
        ax.set_xlabel("% of strategy-asset backtests that FAILED to beat buy & hold")
        ax.set_title("Honest Backtest Census 2026-09-25 - per-strategy fail rate\n"
                     "(stocks slice; survivor-selected famous names; not significance-tested)")
        ax.set_xlim(0, 100)
        fig.tight_layout()
        out = os.path.join(HERE, "strategy_fail_rate.png")
        fig.savefig(out, dpi=120)
        print(f"\n[saved plot -> {out}]")


if __name__ == "__main__":
    main()
