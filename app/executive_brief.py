def generate_executive_brief(df):
    """
    Generate a structured executive procurement brief
    using supplier risk and exposure data.
    """

    highest_risk_supplier = df.sort_values(
        by="supplier_risk_score",
        ascending=False,
    ).iloc[0]

    highest_exposure_supplier = df.sort_values(
        by="normalized_risk_exposure_score",
        ascending=False,
    ).iloc[0]

    high_risk_count = len(df[df["risk_category"] == "High Risk"])
    avg_risk_score = round(df["supplier_risk_score"].mean(), 2)

    highest_risk_category = (
        df.groupby("category")["supplier_risk_score"]
        .mean()
        .sort_values(ascending=False)
    )

    top_category = highest_risk_category.index[0]
    top_category_score = round(highest_risk_category.iloc[0], 2)

    brief = f"""
### Executive Procurement Brief

The current supplier portfolio contains **{len(df)} suppliers**, with **{high_risk_count} high-risk suppliers** and an average supplier risk score of **{avg_risk_score}**.

The highest-risk supplier is **{highest_risk_supplier['supplier_name']}**, with a risk score of **{highest_risk_supplier['supplier_risk_score']}**. This supplier should be reviewed due to elevated operational risk.

The supplier with the highest combined risk and spend exposure is **{highest_exposure_supplier['supplier_name']}**, with a normalized exposure score of **{highest_exposure_supplier['normalized_risk_exposure_score']}**.

The category with the highest average supplier risk is **{top_category}**, with an average risk score of **{top_category_score}**.

Recommended management focus:
- Review high-risk suppliers immediately
- Prioritize suppliers with high risk exposure
- Evaluate alternative suppliers in critical categories
- Monitor category-level supplier concentration
"""

    return brief