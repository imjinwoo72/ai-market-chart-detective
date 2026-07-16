import streamlit as st

st.set_page_config(
    page_title="AI Market Chart Detective",
    page_icon="📈",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Chart",
        "Prediction",
        "About",
    ],
)

if page == "Home":
    st.title("AI Market Chart Detective")

    st.write(
        "Welcome! This application will analyze stock charts "
        "using artificial intelligence."
    )

    st.divider()

    ticker = st.text_input(
        "Ticker Symbol",
        value="AAPL",
    )

    timeframe = st.selectbox(
        "Timeframe",
        [
            "Daily",
            "Weekly",
            "Hourly",
        ],
    )

    lookback = st.selectbox(
        "Lookback",
        [
            "90 Days",
            "180 Days",
            "365 Days",
        ],
    )

    if st.button("Analyze"):
        st.info(
            f"Future analysis for {ticker.upper()} "
            f"using {timeframe} data over {lookback}."
        )

elif page == "Chart":
    st.title("Chart View")

    st.info(
        "The interactive candlestick chart and volume panel "
        "will appear here."
    )

elif page == "Prediction":
    st.title("Prediction & Explanation")

    st.info(
        "The CNN prediction, confidence score, and AI explanation "
        "will appear here."
    )

elif page == "About":
    st.title("About & Methodology")

    st.write(
        "This project will download market data, create chart images, "
        "use a CNN to classify price direction, and explain the result."
    )

    st.warning(
        "This project is for educational purposes and is not financial advice."
    )