def simulate_supplier_failure(supplier_row, portfolio_df):
    """
    Simulate the impact of a supplier failure.
    """

    supplier_name = supplier_row["supplier_name"]
    spend_at_risk = supplier_row["total_spend_usd"]
    category = supplier_row["category"]

    category_suppliers = portfolio_df[
        portfolio_df["category"] == category
    ]

    alternative_count = len(category_suppliers) - 1

    if alternative_count <= 0:
        business_risk = "Critical"
        recommendation = "Immediate sourcing escalation required."
    elif alternative_count <= 2:
        business_risk = "High"
        recommendation = "Identify and qualify backup suppliers urgently."
    elif alternative_count <= 5:
        business_risk = "Medium"
        recommendation = "Review supplier diversification options."
    else:
        business_risk = "Low"
        recommendation = "Supplier base appears sufficiently diversified."

    return {
        "supplier_name": supplier_name,
        "spend_at_risk": spend_at_risk,
        "category": category,
        "alternative_suppliers": alternative_count,
        "business_risk": business_risk,
        "recommendation": recommendation,
    }