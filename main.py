from utils.data_loader import load_data
from strategies.indicators import add_indicators
from strategies.signals import generate_signals
from strategies.backtester import backtest
from models.ml_model import train_model

df = load_data("AAPL")
df = add_indicators(df)
df = generate_signals(df)

model = train_model(df)

print(backtest(df))