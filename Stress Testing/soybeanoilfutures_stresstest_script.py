import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Download latest Soybean Oil Futures data
data = yf.download("ZL=F", period="1y")  # last 1 year of data
latest_price = data['Close'].iloc[-1]    # FIX: use iloc for last value

# 2. Define position size
position_value = 10_000_000  # $10 million long position

# 3. Define stress scenarios (±10%)
scenarios = {
    "-10% Shock": -0.10,
    "Base Case": 0.00,
    "+10% Shock": 0.10
}

# 4. Calculate PnL impact
results = {}
for name, shock in scenarios.items():
    pnl = position_value * shock
    results[name] = pnl

# Convert to DataFrame
results_df = pd.DataFrame.from_dict(results, orient='index', columns=["PnL Impact ($)"])

# 5. Plot
plt.figure(figsize=(8,5))
results_df["PnL Impact ($)"].plot(kind='bar', color=["red","gray","green"])
plt.title("Scenario Analysis: $10m Soybean Oil Long Position")
plt.ylabel("PnL Impact ($)")
plt.axhline(0, color='black', linewidth=0.8)
plt.show()

print("Latest Soybean Oil Price:", latest_price)
print(results_df)
