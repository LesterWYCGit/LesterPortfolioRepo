import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
ticker = "ZL=F"  # Soybean Oil Futures
period = "5y"

# Download data
df = yf.download(ticker, period=period, interval="1d")

# Use Close if Adj Close is not available
if "Adj Close" in df.columns:
    df = df[["Adj Close"]].dropna().rename(columns={"Adj Close": "Close"})
else:
    df = df[["Close"]].dropna()

# Calculate daily returns
df["Returns"] = df["Close"].pct_change()

# Rolling standard deviation (volatility)
df["Vol_30d"] = df["Returns"].rolling(window=30).std()
df["Vol_90d"] = df["Returns"].rolling(window=90).std()

# Plot rolling volatilities
plt.figure(figsize=(12,6))
plt.plot(df.index, df["Vol_30d"], label="30-Day Rolling Volatility", color="blue", alpha=0.7)
plt.plot(df.index, df["Vol_90d"], label="90-Day Rolling Volatility", color="orange", alpha=0.9)

plt.title(f"Rolling Volatility (30d vs 90d) for {ticker}\n({period} Daily Returns)")
plt.xlabel("Date")
plt.ylabel("Volatility (Standard Deviation)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
