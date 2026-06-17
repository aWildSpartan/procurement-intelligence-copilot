from data_loader import load_supplier_data
from scoring import calculate_supplier_risk_scores
from risk_explainer import generate_risk_explanation

def main():
    suppliers = load_supplier_data(
        "data/raw/mock_supplier_performance.csv"
    )

    scored_suppliers = calculate_supplier_risk_scores(suppliers)
    highest_risk_supplier = scored_suppliers.iloc[0]

    explanation = generate_risk_explanation(
        highest_risk_supplier
    )

    print("\nHighest Risk Supplier Analysis\n")

    print(
        f"Supplier: {highest_risk_supplier['supplier_name']}"
    )

    print(
        f"Risk Score: {highest_risk_supplier['supplier_risk_score']}"
    )

    print("\nRisk Drivers:")

    for driver in explanation["risk_drivers"]:
        print(f"- {driver}")

    print(
        f"\nRecommendation: {explanation['recommendation']}"
    )
    print("\nTop 10 Highest-Risk Suppliers:\n")

    print(
        scored_suppliers[
            [
                "supplier_name",
                "supplier_risk_score",
                "risk_category",
            ]
        ].head(10)
    )


if __name__ == "__main__":
    main()