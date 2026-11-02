import streamlit as st

def show_overview():
    st.image("assets/logo.png", width=80)

    st.title("Inventory Demand Prediction")

    st.header("Project Overview")

    st.write("""
Inventory Demand Prediction is a Machine Learning project that predicts
future product demand based on historical inventory and sales information.

The model helps businesses:

- Reduce stock shortages
- Prevent overstocking
- Improve inventory planning
- Optimize warehouse management
- Support business decision making
""")

    st.subheader("Business Problem")

    st.info("""
Retail companies often struggle with balancing inventory levels.

Too much inventory increases storage costs.

Too little inventory results in lost sales.

Machine Learning helps forecast future demand.
""")

    st.subheader("Machine Learning Workflow")

    st.markdown("""
1. Data Collection

2. Data Cleaning

3. Feature Engineering

4. One Hot Encoding

5. Model Training

6. Demand Prediction
""")