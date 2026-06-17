def generate_risk_explanation(supplier):
    """
    Generate a human-readable explanation for a supplier's risk score,
    using both absolute thresholds and category benchmarks.
    """

    risk_drivers = []

    if supplier["on_time_delivery_rate"] < 85:
        risk_drivers.append(
            "Frequent late deliveries are increasing supply risk."
        )

    if supplier["on_time_delivery_vs_category_pct"] < -5:
        risk_drivers.append(
            f"On-time delivery is "
            f"{abs(supplier['on_time_delivery_vs_category_pct'])}% "
            f"below the category average."
        )

    if supplier["defect_rate"] > 4:
        risk_drivers.append(
            "Quality performance is below acceptable standards."
        )

    if supplier["defect_rate_vs_category_pct"] > 25:
        risk_drivers.append(
            f"Defect rate is "
            f"{supplier['defect_rate_vs_category_pct']}% "
            f"above the category average."
        )

    if supplier["average_lead_time_days"] > 45:
        risk_drivers.append(
            "Lead times are significantly longer than preferred."
        )

    if supplier["lead_time_vs_category_pct"] > 25:
        risk_drivers.append(
            f"Lead time is "
            f"{supplier['lead_time_vs_category_pct']}% "
            f"above the category average."
        )

    if supplier["response_time_hours"] > 48:
        risk_drivers.append(
            "Slow responsiveness may delay issue resolution."
        )

    if supplier["response_time_vs_category_pct"] > 25:
        risk_drivers.append(
            f"Response time is "
            f"{supplier['response_time_vs_category_pct']}% "
            f"above the category average."
        )

    if supplier["price_variance_pct"] > 8:
        risk_drivers.append(
            "Pricing is significantly above category averages."
        )

    if not risk_drivers:
        risk_drivers.append(
            "Supplier performance is generally stable compared with peers."
        )

    if supplier["supplier_risk_score"] >= 60:
        recommendation = "Immediate supplier review recommended."
    elif supplier["supplier_risk_score"] >= 30:
        recommendation = "Monitor supplier performance closely."
    else:
        recommendation = "Maintain current supplier relationship."

    return {
        "risk_drivers": risk_drivers,
        "recommendation": recommendation,
    }