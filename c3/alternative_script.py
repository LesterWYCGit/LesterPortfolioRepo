import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Download Soybean Futures data (ticker: ZS=F)
df = yf.download("ZS=F", start="2015-01-01", end="2025-01-01")

# Calculate log returns
df["LogRet"] = np.log1p(df["Adj Close"].pct_change())
df["LogRet"].fillna(0, inplace=True)


# Rolling volatility (30-day and 90-day)
df["30d_vol"] = df["LogRet"].rolling(30).std() * (252**0.5)  # annualized
df["90d_vol"] = df["LogRet"].rolling(90).std() * (252**0.5)

# Plot
plt.figure(figsize=(12,6))
plt.plot(df.index, df["30d_vol"], label="30-Day Volatility", alpha=0.7, color="steelblue")
plt.plot(df.index, df["90d_vol"], label="90-Day Volatility", alpha=0.9, color="orange")

# Highlight stress regimes (30d > 90d)
stress = df["30d_vol"] > df["90d_vol"]
plt.fill_between(df.index, df["30d_vol"], df["90d_vol"], 
                 where=stress, color="red", alpha=0.2, label="Stress Regime")

# Annotate key events
events = {
    "2020-04-01": "COVID-19 Recovery (supply chain)",
    "2022-03-01": "Ukraine War (veg oil shock)",
    "2023-07-01": "El Niño concerns"
}
for date, label in events.items():
    plt.axvline(pd.to_datetime(date), color="gray", linestyle="--", alpha=0.7)
    plt.text(pd.to_datetime(date), plt.ylim()[1]*0.9, label, rotation=90, va="top", ha="right", fontsize=8)

plt.title("Soybean Futures Rolling Volatility (30D vs 90D)")
plt.xlabel("Date")
plt.ylabel("Annualized Volatility")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
