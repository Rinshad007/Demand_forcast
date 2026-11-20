
import plotly.express as px
import pandas as pd
import streamlit as st



df = pd.read_csv("data/demand_forecasting.csv")


def show_chart():

    cl1,cl2,cl3= st.columns(3)

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

    with cl3:
        promtn_dmnd=df.groupby(['Promotion'])['Demand'].mean().reset_index()

        

        fig=px.bar(promtn_dmnd,
                    x="Promotion",
                    y="Demand",
                    title="Demand Over Promotion",
                    color="Promotion"
        )
        fig.update_xaxes(
            tickmode="array",
            tickvals=[0, 1],
            ticktext=["No Promotion", "Promotion"]
        )

        st.plotly_chart(fig, use_container_width='stretch')