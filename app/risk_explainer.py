def generate_risk_explanation(supplier):
    """
    Generate a human-readable explanation for a supplier's risk score.
    """

    risk_drivers = []

    if supplier["on_time_delivery_rate"] < 85:
        risk_drivers.append(
            "Frequent late deliveries are increasing supply risk."
        )

    if supplier["defect_rate"] > 4:
        risk_drivers.append(
            "Quality performance is below acceptable standards."
        )

    if supplier["average_lead_time_days"] > 45:
        risk_drivers.append(
            "Lead times are significantly longer than preferred."
        )

    if supplier["response_time_hours"] > 48:
        risk_drivers.append(
            "Slow responsiveness may delay issue resolution."
        )

    if supplier["price_variance_pct"] > 8:
        risk_drivers.append(
            "Pricing is significantly above category averages."
        )

    if not risk_drivers:
        risk_drivers.append(
            "Supplier performance is generally stable."
        )

    if supplier["supplier_risk_score"] >= 60:
        recommendation = (
            "Immediate supplier review recommended."
        )

    elif supplier["supplier_risk_score"] >= 30:
        recommendation = (
            "Monitor supplier performance closely."
        )

    else:
        recommendation = (
            "Maintain current supplier relationship."
        )

    return {
        "risk_drivers": risk_drivers,
        "recommendation": recommendation,
    }