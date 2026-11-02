import streamlit as st

def show_about():

    st.title("ℹ️ About")

    st.subheader("Developer")

    st.write("**Muhammed Rinshad**")

    st.subheader("Technologies")

    st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib
""")

    st.subheader("Machine Learning Model")

    st.success("Random Forest Regressor")

    st.subheader("Purpose")

    st.write("""
This project demonstrates the use of Machine Learning to forecast inventory demand and assist businesses in inventory planning.
""")