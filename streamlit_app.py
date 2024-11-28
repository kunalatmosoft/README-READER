import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title("📈 Enhanced Real-time Stock Price Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")
ticker = st.sidebar.text_input("Enter Stock Ticker Symbol (e.g., AAPL, TSLA)", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Fetch stock data
if ticker:
    st.subheader(f"Stock Data for {ticker}")
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)

        if not stock_data.empty:
            # Display raw data
            st.write("📋 Data Overview:")
            st.dataframe(stock_data.tail())

            # Moving Averages
            st.sidebar.subheader("Moving Averages")
            ma_periods = st.sidebar.multiselect(
                "Select Moving Average Periods (days):",
                options=[10, 20, 50, 100],
                default=[10, 50],
            )

            # Plot: Closing Price with Moving Averages
            st.write("📊 Price Chart with Moving Averages:")
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data["Close"], label="Closing Price")
            for ma in ma_periods:
                stock_data[f"MA_{ma}"] = stock_data["Close"].rolling(window=ma).mean()
                plt.plot(stock_data[f"MA_{ma}"], label=f"MA {ma} days")
            plt.legend()
            plt.title(f"{ticker} Closing Prices and Moving Averages")
            plt.xlabel("Date")
            plt.ylabel("Price")
            st.pyplot(plt)

            # Volume Chart
            st.write("📈 Volume Chart:")
            st.bar_chart(stock_data["Volume"])

            # Download CSV
            st.write("💾 Download Data:")
            csv = stock_data.to_csv().encode("utf-8")
            st.download_button(
                label="Download as CSV",
                data=csv,
                file_name=f"{ticker}_data.csv",
                mime="text/csv",
            )

            # Statistical Summary
            st.write("📊 Statistical Summary:")
            st.write(stock_data.describe())

        else:
            st.error("No data found for the provided ticker and date range.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Enter a valid stock ticker to begin.")

