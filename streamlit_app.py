import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# App title
st.title("📊 Advanced Stock Price Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")
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

# Fetch and display stock data
if selected_stocks:
    st.subheader("📈 Stock Data Overview")
    try:
        for stock_name in selected_stocks:
            ticker = stock_options[stock_name]
            st.markdown(f"### {stock_name} ({ticker})")
            stock_data = yf.download(ticker, start=start_date, end=end_date)

            if not stock_data.empty:
                # Display data snapshot
                st.write("📋 Data Snapshot:")
                st.dataframe(stock_data.tail())

                # Candlestick Chart
                if show_candlestick:
                    st.write("📊 Candlestick Chart:")
                    fig = go.Figure(data=[
                        go.Candlestick(
                            x=stock_data.index,
                            open=stock_data['Open'],
                            high=stock_data['High'],
                            low=stock_data['Low'],
                            close=stock_data['Close'],
                            name="Candlestick",
                        )
                    ])
                    fig.update_layout(
                        title=f"{stock_name} Candlestick Chart",
                        xaxis_title="Date",
                        yaxis_title="Price",
                        template="plotly_dark",
                    )
                    st.plotly_chart(fig, use_container_width=True)

                # Closing Price Chart
                st.write("📉 Closing Price Chart:")
                st.line_chart(stock_data["Close"])

                # Technical Indicator: Moving Average
                st.sidebar.subheader(f"{stock_name}: Moving Average")
                ma_periods = st.sidebar.multiselect(
                    f"Select Moving Average Periods (days) for {ticker}:",
                    options=[10, 20, 50, 100],
                    default=[20],
                )
                if ma_periods:
                    st.write("📈 Price with Moving Averages:")
                    stock_data_with_ma = stock_data.copy()

                    # Calculate moving averages and validate columns
                    ma_columns = []
                    for ma in ma_periods:
                        col_name = f"MA_{ma}"
                        stock_data_with_ma[col_name] = stock_data["Close"].rolling(ma).mean()
                        if col_name in stock_data_with_ma.columns:
                            ma_columns.append(col_name)

                    # Plot valid columns
                    if ma_columns:
                        st.line_chart(stock_data_with_ma[["Close"] + ma_columns])
                    else:
                        st.warning("No valid moving average data to display. Ensure your data range is sufficient for the selected MA periods.")

                # Volume Chart
                st.write("📊 Volume Chart:")
                st.bar_chart(stock_data["Volume"])

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

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Select at least one stock to begin.")
