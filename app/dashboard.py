from risk_explainer import generate_risk_explanation
from recommendation_engine import generate_supplier_recommendations
from query_engine import answer_procurement_question
from supplier_recommender import recommend_alternative_suppliers
from portfolio_risk import calculate_risk_exposure
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
df = calculate_risk_exposure(df)

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

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Suppliers", len(filtered_df))
col2.metric(
    "High Risk Suppliers",
    len(filtered_df[filtered_df["risk_category"] == "High Risk"]),
)
col3.metric(
    "Average Risk Score",
    round(filtered_df["supplier_risk_score"].mean(), 2),
)
highest_exposure_supplier = filtered_df.sort_values(
    by="normalized_risk_exposure_score",
    ascending=False,
).iloc[0]

col4.metric(
    "Highest Exposure Supplier",
    highest_exposure_supplier["supplier_name"],
)

highest_risk = filtered_df.sort_values(
    by="supplier_risk_score",
    ascending=False,
).iloc[0]

summary_explanation = generate_risk_explanation(highest_risk)
summary_recommendations = generate_supplier_recommendations(highest_risk)

st.info(
    f"Current supplier portfolio contains "
    f"{len(filtered_df[filtered_df['risk_category'] == 'High Risk'])} "
    f"high-risk suppliers, with an average risk score of "
    f"{round(filtered_df['supplier_risk_score'].mean(), 2)}. "
    f"The highest-risk supplier is {highest_risk['supplier_name']}. "
    f"Recommended focus: "
    f"{summary_recommendations['recommended_actions'][0]}"
)

st.subheader("Ask the Procurement Analyst")

user_question = st.text_input(
    "Ask a procurement question",
    placeholder="Example: Which suppliers should I audit first?",
)

if user_question:
    answer = answer_procurement_question(
        user_question,
        filtered_df,
    )

    st.success(answer)

supplier_options = sorted(filtered_df["supplier_name"].unique())

default_supplier = filtered_df.sort_values(
    by="supplier_risk_score",
    ascending=False,
).iloc[0]["supplier_name"]

default_index = supplier_options.index(default_supplier)

selected_supplier = st.sidebar.selectbox(
    "Select Supplier",
    supplier_options,
    index=default_index,
)

supplier_row = filtered_df[
    filtered_df["supplier_name"] == selected_supplier
].iloc[0]

explanation = generate_risk_explanation(supplier_row)
recommendations = generate_supplier_recommendations(supplier_row)

alternative_suppliers = recommend_alternative_suppliers(
    supplier_row,
    filtered_df,
)

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

    st.markdown("### Alternative Suppliers")

    if len(alternative_suppliers) > 0:
        st.dataframe(
            alternative_suppliers[
                [
                    "supplier_name",
                    "supplier_risk_score",
                    "risk_category",
                    "country",
                ]
            ],
            use_container_width=True,
        )
    else:
        st.write("No alternative suppliers available.")

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

st.subheader("Risk Distribution by Category")

category_risk = (
    filtered_df.groupby("category")["supplier_risk_score"]
    .mean()
    .reset_index()
    .sort_values(by="supplier_risk_score", ascending=False)
)

fig_category = px.bar(
    category_risk,
    x="category",
    y="supplier_risk_score",
    title="Average Supplier Risk Score by Category",
)

st.plotly_chart(fig_category, use_container_width=True)

st.subheader("Risk Distribution by Country")

country_risk = (
    filtered_df.groupby("country")["supplier_risk_score"]
    .mean()
    .reset_index()
    .sort_values(by="supplier_risk_score", ascending=False)
)

fig_country = px.bar(
    country_risk,
    x="country",
    y="supplier_risk_score",
    title="Average Supplier Risk Score by Country",
)

st.plotly_chart(fig_country, use_container_width=True)

st.subheader("Spend Exposure vs Supplier Risk")

fig_spend_risk = px.scatter(
    filtered_df,
    x="total_spend_usd",
    y="supplier_risk_score",
    size="order_volume",
    color="risk_category",
    hover_name="supplier_name",
    hover_data=[
        "category",
        "country",
        "on_time_delivery_rate",
        "defect_rate",
        "average_lead_time_days",
    ],
    title="Supplier Risk vs Spend Exposure",
)

st.plotly_chart(fig_spend_risk, use_container_width=True)

st.subheader("Top Supplier Risk Exposure")

top_exposure = filtered_df.sort_values(
    by="normalized_risk_exposure_score",
    ascending=False,
).head(10)

fig_exposure = px.bar(
    top_exposure,
    x="normalized_risk_exposure_score",
    y="supplier_name",
    orientation="h",
    title="Top 10 Suppliers by Normalized Risk Exposure")

st.plotly_chart(fig_exposure, use_container_width=True)

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
            "total_spend_usd",
            "normalized_risk_exposure_score",
        ]
    ].sort_values(by="supplier_risk_score", ascending=False),
    use_container_width=True,
)
