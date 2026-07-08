#!/usr/bin/env python3
"""Carrier-concentration calculator for a tradelane.

Ships with NO data. You (the model) assemble the operator -> service-count (or TEU) mapping from
public sources, pass it in, and this returns HHI + top-N share + a plain-language reading. Count a
parent+subsidiary or a tight consortium as ONE operator before calling this.

Usage:
  python concentration.py '{"Maersk":9,"CMA":9,"COSCO+OOCL":15,"ONE":4,"MSC":2,"others":4}'
  # or pipe JSON on stdin:  echo '{"A":10,"B":3}' | python concentration.py

Output: JSON with hhi, top3_share, n_operators, level, and reading.
"""
import json
import sys


def analyze(shares: dict[str, float]) -> dict:
    counts = {k: float(v) for k, v in shares.items() if float(v) > 0}
    total = sum(counts.values())
    if total <= 0:
        return {"error": "no positive counts provided"}
    pct = {k: 100 * v / total for k, v in counts.items()}
    hhi = round(sum(p * p for p in pct.values()))
    ranked = sorted(pct.items(), key=lambda kv: -kv[1])
    top3 = round(sum(p for _, p in ranked[:3]))
    level = ("fragmented — little pricing power" if hhi < 1500 else
             "moderately concentrated — capacity discipline is feasible" if hhi < 2500 else
             "concentrated — strong scope to hold rates")
    reading = (f"{len(counts)} operators; top-3 hold {top3}% of the trade; HHI {hhi} "
               f"({level}). In an oversupplied market, expect rates to "
               + ("hold/rise here via capacity discipline." if hhi >= 1500
                  else "track the glut down — no one can hold the line."))
    return {"n_operators": len(counts), "hhi": hhi, "top3_share_pct": top3,
            "ranked_pct": [{"operator": k, "pct": round(p, 1)} for k, p in ranked],
            "level": level, "reading": reading}


if __name__ == "__main__":
    raw = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    try:
        data = json.loads(raw)
    except Exception as e:
        print(json.dumps({"error": f"pass a JSON object of operator->count: {e}"}))
        sys.exit(1)
    print(json.dumps(analyze(data), indent=2))
