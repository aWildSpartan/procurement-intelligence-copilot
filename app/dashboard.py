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