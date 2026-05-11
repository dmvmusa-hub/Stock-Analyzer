import streamlit as st
from utils.data_loader import load_data
from strategies.indicators import add_indicators
from strategies.signals import generate_signals
from strategies.backtester import backtest

st.title("AI Trading Dashboard")

ticker = st.selectbox("Asset", ["AAPL", "TSLA", "NVDA", "SPY", "BTC-USD"])

df = load_data(ticker)
df = add_indicators(df)
df = generate_signals(df)

st.subheader("Price Data")
st.dataframe(df.tail())

results = backtest(df)

st.subheader("Backtest Results")
st.write(results)

st.line_chart(df["Close"])