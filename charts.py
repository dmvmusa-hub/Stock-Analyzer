import mplfinance as mpf

def show_chart(df, ticker):
    mpf.plot(
        df,
        type="candle",
        style="charles",
        volume=True,
        title=f"{ticker} Chart",
        mav=(20, 50)
    )