def calculate_risk_exposure(df):
    """
    Calculate normalized supplier portfolio risk exposure based on
    supplier risk score and total spend.
    """

    portfolio_df = df.copy()

    portfolio_df["risk_exposure_value"] = (
        portfolio_df["supplier_risk_score"]
        * portfolio_df["total_spend_usd"]
    )

    min_value = portfolio_df["risk_exposure_value"].min()
    max_value = portfolio_df["risk_exposure_value"].max()

    if max_value == min_value:
        portfolio_df["normalized_risk_exposure_score"] = 0
    else:
        portfolio_df["normalized_risk_exposure_score"] = (
            (
                portfolio_df["risk_exposure_value"] - min_value
            )
            / (max_value - min_value)
            * 100
        ).round(2)

    return portfolio_df.sort_values(
        by="normalized_risk_exposure_score",
        ascending=False,
    )