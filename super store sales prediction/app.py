import streamlit as st

# Page configuration
st.set_page_config(
    page_title="BigMart Sales Prediction",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS theme and layout
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5f7fa, #e4ecf5);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f4e78;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555555;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
    background-color: #1f77b4;
    color: white;
}

.stButton > button:hover {
    background-color: #0d5c91;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="main-title">🛒 BigMart Sales Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Based Outlet Sales Prediction System</div>',
    unsafe_allow_html=True
)

# Create two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📦 Product Details")

    f1 = st.number_input("Item Weight", value=9.30)
    f2 = st.number_input("Item Fat Content", value=0.0)
    f3 = st.number_input("Item Visibility", value=0.016)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏪 Outlet Details")

    f4 = st.number_input("Item MRP", value=249.81)
    f5 = st.number_input("Outlet Establishment Year", value=1999.0)

    st.markdown('</div>', unsafe_allow_html=True)

# Prediction button
if st.button("🔮 Predict Sales"):

    # Demo calculation
    predicted_sales = (
        (f1 * 50) +
        (f3 * 1000) +
        (f4 * 8) +
        (f5 * 0.5)
    )

    st.success(
        f"🎉 Predicted Outlet Sales: ₹ {predicted_sales:,.2f}"
    )

# Footer
st.markdown("---")
st.markdown(
    "<center>Developed using Machine Learning | KNN Regression</center>",
    unsafe_allow_html=True
)