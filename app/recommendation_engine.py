def generate_supplier_recommendations(supplier):
    """
    Generate procurement action recommendations based on supplier risk profile.
    """

    actions = []

    if supplier["supplier_risk_score"] >= 60:
        priority = "High"
        business_impact = "Potential disruption to supply continuity."
        actions.append("Conduct immediate supplier performance review.")
        actions.append("Identify qualified backup suppliers.")
        actions.append("Increase monitoring frequency for this supplier.")

    elif supplier["supplier_risk_score"] >= 30:
        priority = "Medium"
        business_impact = "Supplier performance should be monitored."
        actions.append("Monitor supplier performance trends monthly.")
        actions.append("Request corrective action plan if performance declines.")

    else:
        priority = "Low"
        business_impact = "Supplier relationship appears stable."
        actions.append("Maintain current supplier relationship.")
        actions.append("Review performance during regular supplier reviews.")

    if supplier["on_time_delivery_rate"] < 85:
        actions.append("Review delivery reliability and logistics constraints.")

    if supplier["defect_rate"] > 4:
        actions.append("Schedule quality review or supplier audit.")

    if supplier["average_lead_time_days"] > 45:
        actions.append("Evaluate safety stock or lead time reduction options.")

    if supplier["response_time_hours"] > 48:
        actions.append("Escalate communication expectations with supplier contact.")

    if supplier["price_variance_pct"] > 8:
        actions.append("Review pricing competitiveness against category benchmarks.")

    return {
        "priority": priority,
        "business_impact": business_impact,
        "recommended_actions": actions,
    }