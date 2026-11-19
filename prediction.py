import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/RandomForest1.pkl")
model_columns = joblib.load("model/model_columns1.pkl")
metrics=joblib.load("model/metrics1.pkl")
scaler=joblib.load("model/scaler1.pkl")

def show_prediction():
    st.image("assets/logo.png", width=80)

    st.title("StockWise")

    st.markdown("### Predict Inventory Demand, Optimize Business Decisions")

    st.subheader('Inventory Details')

    col1,col2 = st.columns(2)

    with col1:

        store_id =st.selectbox(
            "Store ID",
             ["S001","S002","S003","S004","S005"]
        )

        inventory = st.number_input("Inventory Level",0.0,10000.0,300.0)

        units = st.number_input("Units Ordered",0.0,10000.0,180.0)

        price = st.number_input("Price",0.0,10000.0,250.0)

        discount = st.number_input("Discount",0.0,100.0,10.0)

        competitor = st.number_input("Competitor Pricing",0.0,10000.0,240.0)

    with col2:

        product_id=st.selectbox(
            "Product ID",
            ['P0001', 'P0002', 'P0003', 'P0004', 'P0005', 'P0006', 'P0007',
             'P0008', 'P0009', 'P0010', 'P0011', 'P0012', 'P0013', 'P0014',
             'P0015', 'P0016', 'P0017', 'P0018', 'P0019', 'P0020']
        )

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

        date = st.date_input("Select date")

    if st.button("Predict Demand"):

        input_df = pd.DataFrame({

            "Product ID":[product_id],
            "Store ID":[store_id],
            "Inventory Level":[inventory],
            "Units Ordered":[units],
            "Price":[price],
            "Discount":[discount],
            "Competitor Pricing":[competitor],
            "Date":[date],
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
        input_scaled=scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]

        st.success(
            f"Predicted Demand : {prediction:.2f} Units"
        )


        available_stock = inventory + units
        stock_balance = available_stock - prediction


        coverage = (available_stock / prediction) * 100 if prediction > 0 else 0

        st.subheader("📦 Inventory Decision Support")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Current Inventory", f"{inventory:.0f} Units")
            st.metric("Incoming Units Ordered", f"{units:.0f} Units")

        with col2:
            st.metric("Available Stock", f"{available_stock:.0f} Units")
            st.metric("Predicted Demand", f"{prediction:.0f} Units")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Stock Coverage", f"{coverage:.1f}%")

        with col2:
            st.metric("Stock Gap", f"{stock_balance:.0f} Units")


        st.progress(min(coverage / 100, 1.0))
        st.caption(f"Stock Coverage: {coverage:.1f}%")

        st.divider()


        if stock_balance >= 0:

            if coverage >= 120:

                st.success("🟢 Excellent Stock Level")

                st.write(f"**Expected Remaining Stock:** {stock_balance:.0f} Units")

                st.info("""
        ### Recommendation

        - Inventory level is excellent.
        - No additional purchase order is required.
        - Continue monitoring demand.
        - Consider reducing future purchase quantities if this trend continues to avoid excess inventory.
        """)

            else:

                st.success("🟢 Sufficient Stock")

                st.write(f"**Expected Remaining Stock:** {stock_balance:.0f} Units")

                st.info("""
        ### Recommendation

        - Current inventory is sufficient to satisfy the predicted demand.
        - No immediate replenishment is required.
        - Continue monitoring demand and supplier deliveries.
        - Review inventory after the next sales cycle.
        """)

        else:

            shortage = abs(stock_balance)

            if coverage >= 90:

                st.warning("🟡 Nearly Sufficient - Monitor Closely")

                st.write(f"**Expected Shortage:** {shortage:.0f} Units")

                st.warning(f"""
        ### Recommendation

        - Available stock is slightly below the predicted demand.
        - Consider ordering **at least {shortage:.0f} additional units**.
        - Monitor supplier deliveries carefully.
        - Review inventory before the demand period begins.
        """)

            else:

                st.error("🔴 High Risk of Stock-out")

                st.write(f"**Expected Shortage:** {shortage:.0f} Units")

                st.error(f"""
        ### Recommendation

        - Place an additional purchase order for **more units**.
        - Contact suppliers immediately to ensure timely replenishment.
        - Monitor inventory closely until new stock arrives.
        - Consider increasing safety stock if high demand continues.
        """)

        st.subheader("📊 Model Performance")

        col1, col2 = st.columns(2)

        col1.metric("R² Score", f"{metrics['R2']:.2f}%")
        col2.metric("MAE", f"{metrics['MAE']:.2f}")


       