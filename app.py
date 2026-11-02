import streamlit as st

from overview import show_overview
from dataset import show_dataset
from prediction import show_prediction
from about import show_about


from utils.styles import load_css





st.set_page_config(
    page_title="Inventory Demand Forecasting",
    page_icon="📦",
    layout="wide"
)


st.markdown(load_css(), unsafe_allow_html=True)


import streamlit as st

with st.sidebar:

    st.image("assets/logo.png", width=80)

    st.markdown("# 📦 Inventory Demand")
    st.markdown("### Forecasting Dashboard")

    st.divider()

    page = st.selectbox(
        "Navigation",
        [
            "Prediction",
            "Project Overview",
            "Dataset Details",
            "About"
        ]
    )

    st.divider()

    st.markdown("### 📊 Model")

    st.success("Random Forest Regressor")

    st.divider()

    st.caption("Developed by Muhammed Rinshad")

if page == "Project Overview":
    show_overview()

elif page == "Dataset Details":
    show_dataset()

elif page == "Prediction":
    show_prediction()

elif page == "About":
    show_about()