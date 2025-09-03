# Moving Average Crossover Analysis for Soybean Oil Futures
# Save this file as: C:\Users\LWYC T14\Desktop\cgcs\c1\ma_crossover_soyoil.py

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# 1. Download Soybean Oil Futures Data
# -----------------------------
ticker = "ZL=F"  # Soybean Oil Futures
df = yf.download(ticker, period="5y", interval="1d")

# Drop rows with missing values
df.dropna(inplace=True)

# -----------------------------
# 2. Calculate Moving Averages
# -----------------------------
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

# -----------------------------
# 3. Identify Crossovers
# -----------------------------
df['Signal'] = 0
df['Signal'] = df['MA20'] > df['MA50']
df['Crossover'] = df['Signal'].diff()

# -----------------------------
# 4. Plot Price with MAs
# -----------------------------
plt.figure(figsize=(14,7))
plt.plot(df.index, df['Close'], label=f'{ticker} Price', color='black', alpha=0.7)
plt.plot(df.index, df['MA20'], label='20-Day MA', color='blue')
plt.plot(df.index, df['MA50'], label='50-Day MA', color='red')

# Mark Bullish and Bearish Crossovers
plt.plot(df[df['Crossover'] == 1].index, 
         df['MA20'][df['Crossover'] == 1], 
         '^', markersize=10, color='green', label='Bullish Crossover')

plt.plot(df[df['Crossover'] == -1].index, 
         df['MA20'][df['Crossover'] == -1], 
         'v', markersize=10, color='red', label='Bearish Crossover')

plt.title(f'{ticker} Moving Average Crossover (Bullish/Bearish Signals)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
