
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Downloading and Importing dataset
# Download Soybean historical data 

ticker = "ZS=F"
data = yf.download(ticker, start="2024-01-01", end="2025-08-01")

# Ensure the column exists (some versions may have 'Adj Close' or 'Close')
if 'Adj Close' in data.columns:
    price_col = 'Adj Close'
elif 'Close' in data.columns:
    price_col = 'Close'
else:
    raise KeyError("No 'Adj Close' or 'Close' column found in downloaded data")

# Step 2: Generating Key Metrics 
#         Daily Returns, Moving Average, Volatility 

data['Daily_Return'] = data[price_col].pct_change() * 100  # daily % change
data['MA_7'] = data[price_col].rolling(window=7).mean()   # 7-day moving average
data['MA_30'] = data[price_col].rolling(window=30).mean() # 30-day moving average
data['Volatility_7'] = data['Daily_Return'].rolling(window=7).std()
data['Volatility_30'] = data['Daily_Return'].rolling(window=30).std()

# Step 3: Save cleaned dataset with metrics
data.to_csv("CommoditiesAnalysis/commodities_historical_price.csv")
print("Saved commodities_historical_price.csv")

# Step 4: Quick plot to visualize price trend (Display of my understanding with matplotlib)
plt.figure(figsize=(12,6))
plt.plot(data[price_col], label=f'{price_col}')
plt.plot(data['MA_7'], label='7-Day MA')
plt.plot(data['MA_30'], label='30-Day MA')
plt.title('Soybean Futures Price Trend')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()