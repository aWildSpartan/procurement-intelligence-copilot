import pandas as pd


def normalize_series(series: pd.Series) -> pd.Series:
    """
    Normalize a numeric pandas Series to a 0-100 scale.
    If all values are equal, return 0 for all rows.
    """
    min_value = series.min()
    max_value = series.max()

    if max_value == min_value:
        return pd.Series([0] * len(series), index=series.index)

    return ((series - min_value) / (max_value - min_value)) * 100


def assign_risk_category(risk_score: float) -> str:
    """
    Convert numeric supplier risk score into a category.
    """
    if risk_score <= 30:
        return "Low Risk"
    elif risk_score <= 60:
        return "Medium Risk"
    return "High Risk"


def calculate_supplier_risk_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate supplier risk scores based on delivery, quality,
    lead time, price variance, and responsiveness.
    """
    scored_df = df.copy()

    scored_df["delivery_risk"] = 100 - scored_df["on_time_delivery_rate"]
    scored_df["quality_risk"] = normalize_series(scored_df["defect_rate"])
    scored_df["lead_time_risk"] = normalize_series(scored_df["average_lead_time_days"])
    scored_df["price_risk"] = normalize_series(scored_df["price_variance_pct"].abs())
    scored_df["responsiveness_risk"] = normalize_series(scored_df["response_time_hours"])

    scored_df["supplier_risk_score"] = (
        0.30 * scored_df["delivery_risk"]
        + 0.25 * scored_df["quality_risk"]
        + 0.20 * scored_df["lead_time_risk"]
        + 0.15 * scored_df["price_risk"]
        + 0.10 * scored_df["responsiveness_risk"]
    ).round(2)

    scored_df["risk_category"] = scored_df["supplier_risk_score"].apply(assign_risk_category)

    return scored_df.sort_values(by="supplier_risk_score", ascending=False)
    