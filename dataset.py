import streamlit as st
import pandas as pd

from chart import show_chart


def show_dataset():

    st.title("📂 Dataset Details")

    # Load dataset
    df = pd.read_csv("data/demand_forecasting.csv")


    col1, col2 = st.columns(2)

    with col1:
            st.metric("Total Rows", df.shape[0])

    with col2:
            st.metric("Total Columns", df.shape[1])

    print(df.columns)

    st.subheader("Dataset Rows")

    st.dataframe(df.head(), use_container_width=True)

    df = pd.DataFrame({
    
            "Feature":[
                "Inventory Level",
                "Units Ordered",
                "Price",
                "Discount",
                "Competitor Pricing",
                "Category",
                "Weather Condition",
                "Seasonality",
                "Promotion",
                "Month",
                "Demand Forecast"
            ],
    
            "Type":[
                "Numeric",
                "Numeric",
                "Numeric",
                "Numeric",
                "Numeric",
                "Categorical",
                "Categorical",
                "Categorical",
                "Binary",
                "Numeric",
                "Target"
            ]
    
        })
    
    st.subheader("Dataset Features")
    
    st.dataframe(df,use_container_width=True)
    
    st.subheader("Target Variable")
    
    st.success("DemandS")

    st.subheader("📊 CHARTS ")
    
    show_chart()
    
   