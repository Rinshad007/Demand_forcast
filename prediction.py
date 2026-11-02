import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/RandomForest.pkl")
model_columns = joblib.load("model/rf_model_columns.pkl")
metrics=joblib.load("model/metrics.pkl")

def show_prediction():
    st.image("assets/logo.png", width=80)

    st.title("Inventory Demand Prediction")

    st.subheader('Inventory Details')

    col1,col2 = st.columns(2)

    with col1:

        inventory = st.number_input("Inventory Level",0.0,10000.0,300.0)

        units = st.number_input("Units Ordered",0.0,10000.0,180.0)

        price = st.number_input("Price",0.0,10000.0,250.0)

        discount = st.number_input("Discount",0.0,100.0,10.0)

        competitor = st.number_input("Competitor Pricing",0.0,10000.0,240.0)

    with col2:

        category = st.selectbox(
            "Category",
            ["Electronics","Furniture","Groceries","Toys","Clothing"]
        )

        weather = st.selectbox(
            "Weather",
            ["Sunny","Rainy","Cloudy","Snowy"]
        )

        season = st.selectbox(
            "Seasonality",
            ["Spring","Summer","Autumn","Winter"]
        )

        promotion = st.selectbox("Promotion",[0,1])

        month = st.number_input("Month",1,12,1)

    if st.button("Predict Demand"):

        input_df = pd.DataFrame({

            "Inventory Level":[inventory],
            "Units Ordered":[units],
            "Price":[price],
            "Discount":[discount],
            "Competitor Pricing":[competitor],
            "Month":[month],
            "Category":[category],
            "Weather Condition":[weather],
            "Seasonality":[season],
            "Promotion":[promotion]

        })

        input_df = pd.get_dummies(input_df)

        input_df = input_df.reindex(
            columns=model_columns,
            fill_value=0
        )

        prediction = model.predict(input_df)[0]

        st.success(
            f"Predicted Demand : {prediction:.2f} Units"
        )


        st.subheader("📊 Model Performance")

        col1, col2 = st.columns(2)

        col1.metric("R² Score", f"{metrics['R2']:.2f}%")
        col2.metric("MAE", f"{metrics['MAE']:.2f}")


       