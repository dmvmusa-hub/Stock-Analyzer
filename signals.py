def generate_signals(df):
    df["Signal"] = 0

    df.loc[df["SMA_20"] > df["SMA_50"], "Signal"] = 1
    df.loc[df["SMA_20"] < df["SMA_50"], "Signal"] = -1

    df.loc[df["RSI"] < 30, "Signal"] = 1
    df.loc[df["RSI"] > 70, "Signal"] = -1

    return df