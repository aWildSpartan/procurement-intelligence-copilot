def compare_suppliers(supplier_a, supplier_b):
    """
    Compare two suppliers and recommend the lower-risk option.
    """

    if (
        supplier_a["supplier_risk_score"]
        < supplier_b["supplier_risk_score"]
    ):
        recommended_supplier = supplier_a["supplier_name"]
    else:
        recommended_supplier = supplier_b["supplier_name"]

    comparison_data = {
        "Supplier A": supplier_a["supplier_name"],
        "Supplier B": supplier_b["supplier_name"],
        "Risk Score A": supplier_a["supplier_risk_score"],
        "Risk Score B": supplier_b["supplier_risk_score"],
        "On Time Delivery A": supplier_a["on_time_delivery_rate"],
        "On Time Delivery B": supplier_b["on_time_delivery_rate"],
        "Defect Rate A": supplier_a["defect_rate"],
        "Defect Rate B": supplier_b["defect_rate"],
        "Lead Time A": supplier_a["average_lead_time_days"],
        "Lead Time B": supplier_b["average_lead_time_days"],
        "Spend A": supplier_a["total_spend_usd"],
        "Spend B": supplier_b["total_spend_usd"],
        "Recommended Supplier": recommended_supplier,
    }

    return comparison_data