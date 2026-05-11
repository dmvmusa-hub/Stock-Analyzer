def backtest(df, starting_balance=10000):
    balance = starting_balance
    position = 0

    wins = 0
    losses = 0

    for i in range(len(df)):

        signal = df["Signal"].iloc[i]
        price = df["Close"].iloc[i]

        if signal == 1 and position == 0:
            position = balance / price
            balance = 0
            entry = price

        elif signal == -1 and position > 0:
            balance = position * price

            if price > entry:
                wins += 1
            else:
                losses += 1

            position = 0

    final = balance if balance > 0 else position * df["Close"].iloc[-1]

    return {
        "Final Balance": round(final, 2),
        "Wins": wins,
        "Losses": losses
    }