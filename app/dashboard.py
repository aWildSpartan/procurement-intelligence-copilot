from risk_explainer import generate_risk_explanation
from recommendation_engine import generate_supplier_recommendations
import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Procurement Intelligence Copilot",
    layout="wide",
)

st.title("Procurement Intelligence Copilot")
st.subheader("Supplier Risk Dashboard")

df = pd.read_csv("data/processed/scored_supplier_performance.csv")

risk_filter = st.sidebar.multiselect(
    "Filter by Risk Category",
    options=df["risk_category"].unique(),
    default=df["risk_category"].unique(),
)

category_filter = st.sidebar.multiselect(
    "Filter by Category",
    options=df["category"].unique(),
    default=df["category"].unique(),
)

filtered_df = df[
    (df["risk_category"].isin(risk_filter))
    & (df["category"].isin(category_filter))
]

col1, col2, col3 = st.columns(3)

col1.metric("Total Suppliers", len(filtered_df))
col2.metric(
    "High Risk Suppliers",
    len(filtered_df[filtered_df["risk_category"] == "High Risk"]),
)
col3.metric(
    "Average Risk Score",
    round(filtered_df["supplier_risk_score"].mean(), 2),
)

selected_supplier = st.sidebar.selectbox(
    "Select Supplier",
    sorted(filtered_df["supplier_name"].unique()),
)

supplier_row = filtered_df[
    filtered_df["supplier_name"] == selected_supplier
].iloc[0]

explanation = generate_risk_explanation(supplier_row)
recommendations = generate_supplier_recommendations(supplier_row)

st.divider()

st.subheader("Supplier Intelligence Panel")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Supplier", supplier_row["supplier_name"])
col2.metric("Category", supplier_row["category"])
col3.metric("Country", supplier_row["country"])
col4.metric("Risk Category", supplier_row["risk_category"])

col5, col6, col7, col8 = st.columns(4)

col5.metric("Risk Score", supplier_row["supplier_risk_score"])
col6.metric(
    "Lead Time vs Category",
    f"{supplier_row['lead_time_vs_category_pct']}%",
)
col7.metric(
    "Defect Rate vs Category",
    f"{supplier_row['defect_rate_vs_category_pct']}%",
)
col8.metric(
    "Response Time vs Category",
    f"{supplier_row['response_time_vs_category_pct']}%",
)

left_col, right_col = st.columns(2)

with left_col:
    st.markdown("### Risk Drivers")
    for driver in explanation["risk_drivers"]:
        st.write(f"- {driver}")

with right_col:
    st.markdown("### Recommended Actions")
    for action in recommendations["recommended_actions"]:
        st.write(f"- {action}")

    st.markdown(f"**Priority:** {recommendations['priority']}")
    st.markdown(f"**Business Impact:** {recommendations['business_impact']}")

st.divider()

st.subheader("Top Supplier Risks")

top_risk = filtered_df.sort_values(
    by="supplier_risk_score",
    ascending=False,
).head(10)

fig = px.bar(
    top_risk,
    x="supplier_risk_score",
    y="supplier_name",
    orientation="h",
    title="Top 10 Highest-Risk Suppliers",
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Supplier Risk Table")

st.dataframe(
    filtered_df[
        [
            "supplier_name",
            "category",
            "country",
            "supplier_risk_score",
            "risk_category",
            "on_time_delivery_rate",
            "defect_rate",
            "average_lead_time_days",
            "response_time_hours",
        ]
    ].sort_values(by="supplier_risk_score", ascending=False),
    use_container_width=True,
)
