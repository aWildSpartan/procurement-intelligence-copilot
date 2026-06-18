def recommend_alternative_suppliers(selected_supplier, df, max_results=3):
    """
    Recommend lower-risk alternative suppliers from the same category.
    """

    category = selected_supplier["category"]
    supplier_name = selected_supplier["supplier_name"]

    alternatives = df[
        (df["category"] == category)
        & (df["supplier_name"] != supplier_name)
    ].copy()

    alternatives = alternatives.sort_values(
        by="supplier_risk_score",
        ascending=True,
    )

    return alternatives.head(max_results)