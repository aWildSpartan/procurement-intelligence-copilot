def answer_procurement_question(question, df):
    """
    Simple rule-based query engine for procurement analytics questions.
    """

    question_lower = question.lower()

    if "highest risk" in question_lower or "riskiest supplier" in question_lower:
        supplier = df.sort_values(
            by="supplier_risk_score",
            ascending=False,
        ).iloc[0]

        return (
            f"The highest-risk supplier is {supplier['supplier_name']} "
            f"with a risk score of {supplier['supplier_risk_score']} "
            f"and a risk category of {supplier['risk_category']}."
        )

    if "audit" in question_lower:
        high_risk_suppliers = df[
            df["risk_category"] == "High Risk"
        ].sort_values(
            by="supplier_risk_score",
            ascending=False,
        )

        suppliers = ", ".join(
            high_risk_suppliers["supplier_name"].head(5).tolist()
        )

        return (
            f"Recommended suppliers for audit: {suppliers}. "
            f"These suppliers have the highest risk scores in the portfolio."
        )

    if "category" in question_lower and "risk" in question_lower:
        category_risk = (
            df.groupby("category")["supplier_risk_score"]
            .mean()
            .sort_values(ascending=False)
        )

        top_category = category_risk.index[0]
        top_score = round(category_risk.iloc[0], 2)

        return (
            f"The category with the highest average supplier risk is "
            f"{top_category}, with an average risk score of {top_score}."
        )

    if "country" in question_lower and "risk" in question_lower:
        country_risk = (
            df.groupby("country")["supplier_risk_score"]
            .mean()
            .sort_values(ascending=False)
        )

        top_country = country_risk.index[0]
        top_score = round(country_risk.iloc[0], 2)

        return (
            f"The country with the highest average supplier risk is "
            f"{top_country}, with an average risk score of {top_score}."
        )

    if "spend" in question_lower and "risk" in question_lower:
        high_exposure = df.sort_values(
            by=["supplier_risk_score", "total_spend_usd"],
            ascending=False,
        ).head(5)

        suppliers = ", ".join(
            high_exposure["supplier_name"].tolist()
        )

        return (
            f"The suppliers with the highest combined risk and spend exposure are: "
            f"{suppliers}."
        )

    return (
        "I can currently answer questions about highest-risk suppliers, "
        "supplier audits, category risk, country risk, and spend exposure."
    )