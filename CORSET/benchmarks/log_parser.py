import json
import os
import sys


def analyze_benchmarks(file_path="benchmarks/results.json"):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Run 'npx promptfoo eval' first.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    metrics = {}
    results = data.get("results", {}).get("table", {}).get("body", [])

    for row in results:
        scenario = row.get("scenario", {}).get("name", "Unknown")
        tokens = row.get("response", {}).get("tokenUsage", {}).get("total", 0)
        output_text = row.get("response", {}).get("output", "")
        loc = len(output_text.strip().split("\n")) if output_text else 0

        if scenario not in metrics:
            metrics[scenario] = {"tokens": 0, "loc": 0, "count": 0}

        metrics[scenario]["tokens"] += tokens
        metrics[scenario]["loc"] += loc
        metrics[scenario]["count"] += 1

    print("\n=========================================")
    print("      CORSET BENCHMARK SCORECARD         ")
    print("=========================================\n")

    baseline = metrics.get("Baseline (Default)")

    for scenario, data in metrics.items():
        avg_tokens = data["tokens"] / data["count"] if data["count"] else 0
        avg_loc = data["loc"] / data["count"] if data["count"] else 0

        print(f"[{scenario}]")
        print(f"  ├── Avg Total Tokens: {avg_tokens:.1f}")
        print(f"  └── Avg Output Lines: {avg_loc:.1f}")

        if baseline and scenario != "Baseline (Default)":
            base_tokens = baseline["tokens"] / baseline["count"]
            token_savings = ((base_tokens - avg_tokens) / base_tokens) * 100
            print(f"  └── Token Reduction:  {token_savings:.1f}%\n")


if __name__ == "__main__":
    analyze_benchmarks()
