def calculate_risk_exposure(df):
    """
    Calculate supplier portfolio risk exposure.
    """

    portfolio_df = df.copy()

    portfolio_df["risk_exposure_score"] = (
        portfolio_df["supplier_risk_score"]
        * portfolio_df["total_spend_usd"]
    )

    return portfolio_df.sort_values(
        by="risk_exposure_score",
        ascending=False,
    )