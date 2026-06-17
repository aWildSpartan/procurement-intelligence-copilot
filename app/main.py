from data_loader import load_supplier_data
from scoring import calculate_supplier_risk_scores


def main():
    suppliers = load_supplier_data(
        "data/raw/mock_supplier_performance.csv"
    )

    scored_suppliers = calculate_supplier_risk_scores(suppliers)

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