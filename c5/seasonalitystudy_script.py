import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ---- Settings ----
tickers = ["ZC=F", "ZW=F"]   # Corn & Wheat futures
start_date = "2013-01-01"

# ---- Download Data ----
data = yf.download(tickers, start=start_date)["Close"]

# ---- Calculate Monthly Returns ----
monthly = data.resample("M").last()
monthly_returns = monthly.pct_change()

# ---- Group by Month Across Years ----
monthly_returns["month"] = monthly_returns.index.month
avg_monthly = monthly_returns.groupby("month").mean()

# ---- Plot ----
plt.figure(figsize=(12,6))
avg_monthly.plot(kind="bar", width=0.8)

plt.title("Average Monthly Returns (Corn & Wheat) - Last 10Y+")
plt.ylabel("Average Return")
plt.xlabel("Month")
plt.xticks(range(0,12), 
           ["Jan","Feb","Mar","Apr","May","Jun",
            "Jul","Aug","Sep","Oct","Nov","Dec"], rotation=45)

plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend(title="Ticker")
plt.tight_layout()
plt.show()
