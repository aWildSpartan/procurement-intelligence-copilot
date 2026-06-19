def generate_procurement_opportunities(df):
    """
    Identify procurement opportunities based on supplier risk,
    spend exposure, and supplier concentration.
    """

    opportunities = []

    high_spend_threshold = df["total_spend_usd"].quantile(0.75)

    for _, supplier in df.iterrows():
        supplier_name = supplier["supplier_name"]
        category = supplier["category"]

        category_supplier_count = len(
            df[df["category"] == category]
        )

        if supplier["risk_category"] == "High Risk":
            opportunities.append(
                {
                    "supplier": supplier_name,
                    "category": category,
                    "opportunity": "Risk Reduction",
                    "estimated_impact": "High",
                    "recommended_action": (
                        "Prioritize supplier review, corrective action plan, "
                        "or backup supplier qualification."
                    ),
                }
            )

        elif (
            supplier["total_spend_usd"] >= high_spend_threshold
            and supplier["risk_category"] == "Medium Risk"
        ):
            opportunities.append(
                {
                    "supplier": supplier_name,
                    "category": category,
                    "opportunity": "Supplier Development",
                    "estimated_impact": "Medium",
                    "recommended_action": (
                        "Engage supplier to improve reliability, quality, "
                        "or responsiveness before risk escalates."
                    ),
                }
            )

        elif (
            supplier["total_spend_usd"] >= high_spend_threshold
            and supplier["risk_category"] == "Low Risk"
        ):
            opportunities.append(
                {
                    "supplier": supplier_name,
                    "category": category,
                    "opportunity": "Contract Renegotiation",
                    "estimated_impact": "Medium",
                    "recommended_action": (
                        "Explore pricing, volume, or service-level improvements "
                        "with a stable high-spend supplier."
                    ),
                }
            )

        if category_supplier_count <= 2:
            opportunities.append(
                {
                    "supplier": supplier_name,
                    "category": category,
                    "opportunity": "Supplier Diversification",
                    "estimated_impact": "High",
                    "recommended_action": (
                        "Identify additional qualified suppliers to reduce "
                        "single-category dependency."
                    ),
                }
            )

    return opportunities