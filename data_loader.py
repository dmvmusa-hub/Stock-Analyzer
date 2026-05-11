# This library downloads stock data from Yahoo Finance
import yfinance as yf

# Pandas helps organize data into tables
import pandas as pd


def load_data(ticker="AAPL", period="1y", interval="1d"):
    """
    Downloads historical market data.

    ticker:
        Stock symbol like AAPL or TSLA

    period:
        How much historical data to download

    interval:
        Candle timeframe
    """

    data = yf.download(
        ticker,
        period=period,
        interval=interval
    )

    # Remove missing rows
    data.dropna(inplace=True)

    return data