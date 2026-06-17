import pandas as pd


def add_category_benchmarks(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add category-level benchmark metrics to supplier performance data.
    """
    benchmarked_df = df.copy()

    category_benchmarks = benchmarked_df.groupby("category").agg(
        category_avg_on_time_delivery=("on_time_delivery_rate", "mean"),
        category_avg_defect_rate=("defect_rate", "mean"),
        category_avg_lead_time=("average_lead_time_days", "mean"),
        category_avg_response_time=("response_time_hours", "mean"),
        category_avg_price_variance=("price_variance_pct", "mean"),
    )

    benchmarked_df = benchmarked_df.merge(
        category_benchmarks,
        on="category",
        how="left",
    )

    benchmarked_df["lead_time_vs_category_pct"] = (
        (
            benchmarked_df["average_lead_time_days"]
            - benchmarked_df["category_avg_lead_time"]
        )
        / benchmarked_df["category_avg_lead_time"]
        * 100
    ).round(2)

    benchmarked_df["defect_rate_vs_category_pct"] = (
        (
            benchmarked_df["defect_rate"]
            - benchmarked_df["category_avg_defect_rate"]
        )
        / benchmarked_df["category_avg_defect_rate"]
        * 100
    ).round(2)

    benchmarked_df["response_time_vs_category_pct"] = (
        (
            benchmarked_df["response_time_hours"]
            - benchmarked_df["category_avg_response_time"]
        )
        / benchmarked_df["category_avg_response_time"]
        * 100
    ).round(2)

    benchmarked_df["on_time_delivery_vs_category_pct"] = (
        (
            benchmarked_df["on_time_delivery_rate"]
            - benchmarked_df["category_avg_on_time_delivery"]
        )
        / benchmarked_df["category_avg_on_time_delivery"]
        * 100
    ).round(2)

    return benchmarked_df