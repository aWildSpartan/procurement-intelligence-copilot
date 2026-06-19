def compare_suppliers(supplier_a, supplier_b):
    """
    Compare two suppliers and recommend the stronger procurement option.
    """

    if supplier_a["supplier_risk_score"] < supplier_b["supplier_risk_score"]:
        recommended_supplier = supplier_a["supplier_name"]
        risk_gap = round(
            supplier_b["supplier_risk_score"]
            - supplier_a["supplier_risk_score"],
            2,
        )
    else:
        recommended_supplier = supplier_b["supplier_name"]
        risk_gap = round(
            supplier_a["supplier_risk_score"]
            - supplier_b["supplier_risk_score"],
            2,
        )

    recommendation_summary = (
        f"Prefer {recommended_supplier} based on a "
        f"{risk_gap}-point lower supplier risk score."
    )

    return {
        "recommended_supplier": recommended_supplier,
        "risk_gap": risk_gap,
        "recommendation_summary": recommendation_summary,
    }