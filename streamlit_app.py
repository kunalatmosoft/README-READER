import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# App title
st.title("📊 Enhanced Stock Price Dashboard")

# Sidebar for user input
st.sidebar.header("Settings")
stock_options = {
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Tesla (TSLA)": "TSLA",
    "Amazon (AMZN)": "AMZN",
    "Google (GOOGL)": "GOOGL",
    "Netflix (NFLX)": "NFLX",
    "NVIDIA (NVDA)": "NVDA",
}
selected_stocks = st.sidebar.multiselect(
    "Select Stock Ticker(s):",
    options=stock_options.keys(),
    default=["Apple (AAPL)"],
)
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

show_candlestick = st.sidebar.checkbox("Show Candlestick Chart", value=True)
show_volume = st.sidebar.checkbox("Show Volume Chart", value=True)

# Check valid date range
if start_date >= end_date:
    st.error("The start date must be earlier than the end date. Please adjust the dates.")
else:
    if selected_stocks:
        st.subheader("📈 Stock Data Overview")
        for stock_name in selected_stocks:
            ticker = stock_options[stock_name]
            st.markdown(f"### {stock_name} ({ticker})")
            
            # Download stock data
            stock_data = yf.download(ticker, start=start_date, end=end_date)
            
            if not stock_data.empty:
                # Reset index to avoid multi-index issues
                stock_data.reset_index(inplace=True)

                # Display data snapshot
                st.write("📋 Data Snapshot:")
                st.dataframe(stock_data.tail())

                # Candlestick Chart
                if show_candlestick:
                    st.write("📊 Candlestick Chart:")
                    fig = go.Figure(
                        data=[
                            go.Candlestick(
                                x=stock_data['Date'],
                                open=stock_data['Open'],
                                high=stock_data['High'],
                                low=stock_data['Low'],
                                close=stock_data['Close'],
                                name="Candlestick",
                            )
                        ]
                    )
                    fig.update_layout(
                        title=f"{stock_name} Candlestick Chart",
                        xaxis_title="Date",
                        yaxis_title="Price",
                        template="plotly_white",
                    )
                    st.plotly_chart(fig, use_container_width=True)

                # Moving Averages
                st.sidebar.subheader(f"{stock_name}: Moving Average")
                ma_periods = st.sidebar.multiselect(
                    f"Select Moving Average Periods (days) for {ticker}:",
                    options=[10, 20, 50, 100],
                    default=[20],
                )
                if ma_periods:
                    st.write("📈 Price with Moving Averages:")
                    stock_data_with_ma = stock_data.copy()

                    # Calculate and plot moving averages
                    for ma in ma_periods:
                        stock_data_with_ma[f"MA_{ma}"] = stock_data_with_ma["Close"].rolling(window=ma).mean()

                    # Display line chart with moving averages
                    ma_columns = [f"MA_{ma}" for ma in ma_periods]
                    st.line_chart(stock_data_with_ma.set_index("Date")[["Close"] + ma_columns])

                # Volume Chart
                if show_volume:
                    st.write("📊 Volume Chart:")
                    st.bar_chart(stock_data.set_index("Date")["Volume"])

                # Download CSV
                st.write("💾 Download Data:")
                csv = stock_data.to_csv().encode("utf-8")
                st.download_button(
                    label=f"Download {ticker} Data as CSV",
                    data=csv,
                    file_name=f"{ticker}_data.csv",
                    mime="text/csv",
                )
            else:
                st.error(f"No data found for {ticker} in the specified date range.")
    else:
        st.info("Please select at least one stock to view data.")
