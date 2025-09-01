# 🌾 Soybean Futures Analysis

This project downloads, cleans, and analyzes Soybean Futures (ZS=F) historical price data using yfinance.
It computes key metrics (returns, moving averages, volatility), saves a cleaned dataset, and generates visualizations to understand price trends.

📌  Source of Data: [YahooFinance](https://finance.yahoo.com/quote/ZS=F/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMXPbnaPvuQs1c1vamN0hoMMD7--UCoGbMXwhUMZH9GwCHkbAD3Oxl1TmFIWA3GaqvC4ji7Kt1LM0TPyrffheAhzqPbHSWeHQQzPXVkuBc9iMIuqZ8MkCloByrjDuvWxaGXuE5oz3fGXnktsE8nreJ0699LQRPZTY1hPztD-zmnN)

## Features

Data Download: Fetches historical Soybean Futures prices from Yahoo Finance (yfinance).

Metrics Computation:
Daily returns (% change): Calculated percentage change in price day-to-day to monitor short-term fluctuations and guide risk management.
7-day and 30-day moving averages: Smoothed prices to identify short- and long-term trends, helping traders and procurement teams time purchases and sales strategically.
7-day and 30-day rolling volatility: Measured standard deviation of daily returns to assess price risk, inform hedging decisions, and optimize option or futures strategies.
Data Export: Saves a cleaned dataset with calculated metrics to CSV.
Visualization: Plots historical price trend with short-term and long-term moving averages.

Chart
Blue = Soybean Futures closing price
Orange = 7-day moving average
Green = 30-day moving average

## Future Enhancements
Add Sharpe ratio for risk-adjusted returns
Add cumulative returns for long-term performance
Export summary statistics (mean, volatility, min/max)