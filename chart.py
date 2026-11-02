
import plotly.express as px
import pandas as pd
import streamlit as st



df = pd.read_csv("data/demand_forecasting.csv")


def show_chart():

    cl1,cl2,= st.columns(2)

    with cl1:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Month"] = df["Date"].dt.month
        month_df = df.groupby("Month")["Demand"].mean().reset_index()
        fig = px.line(
            month_df,
            x="Month",
            y="Demand",
            markers=True,
            title="Monthly Average Demand"
        )
    
        st.plotly_chart(fig, use_container_width='stretch')


    with cl2:
        category_df = df.groupby("Category")["Demand"].mean().reset_index()
        fig = px.bar(
            category_df,
            x="Category",
            y="Demand",
            title="Average Demand by Category",
            color="Category"
        )

        st.plotly_chart(fig, use_container_width='stretch')
