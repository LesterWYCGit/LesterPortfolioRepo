import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define tickers
tickers = ['ZL=F', 'CL=F', 'ZC=F']

# Fetch historical data
data = yf.download(tickers, start='2010-01-01', end='2025-09-03')['Close']

# Calculate daily returns
returns = data.pct_change().dropna()

# Compute correlation matrix
corr_matrix = returns.corr()

# Plot correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix: Soybean Oil, Crude Oil, and Corn')
plt.show()
