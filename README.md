# LesterPortfolioRepo

🔍 About This Repository & [Me](https://www.linkedin.com/in/lester-wee-yi-cheng-6a0074185/)

This repository is designed to showcase how I approach common data challenges that firms encounter, including data aggregation, anomaly detection, and data quality issues such as duplicates, inconsistent formats, or missing values. Using Python and VS Code, I demonstrate practical steps to identify, clean, and validate data, ensuring that it is reliable and actionable for analysis or decision-making. I also focus on documenting the workflow clearly, which is a critical part of data governance ensuring that others can understand and reproduce the process, while maintaining a level of transaprency. 

While some firms may use different software or platforms, I have a general understanding of standard workflows, and I’m actively developing my statistics knowledge to better interpret trends, measure variability, and support informed decisions. Through these projects, I aim to show not only technical skills but also a thoughtful approach to real-world data problems, which includes knowing when to automate solutions, when to collaborate with other teams, and how to prioritize data quality to support business objectives.

🎯In short:

Technical execution: Python, VS Code, NumPy, Pandas, Data Wrangling
Data governance awareness: documenting workflows, reproducibility
Analytical mindset: recognizing anomalies, thinking about statistics
Practical business sense: when to automate vs involve others, decision-support focus

DEMO/ Case Study

<details>
<summary>🏦 Loan Application Data Cleaning
Folder: LoanRejectionApproval 
Dataset Source: [here](https://www.kaggle.com/datasets/bsugiarto9/loan-status-prediction-with-added-nans)
📌 Summary
Imported loan application data with Pandas, checked for missing values and duplicates, and flagged applications with incomplete information by pushing them to the bottom for review. While no deep insights were derived, this project demonstrates the ability to wrangle and clean raw financial data to ensure accuracy and completeness, to be incompliance with Regulatory/ Compliance Checks.
</details>
---

<details>
    <summary>🌾 Commodities Price Analysis — Soybean Futures
Dataset Source: [Yahoo Finance](https://finance.yahoo.com/quote/ZS=F/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAMXPbnaPvuQs1c1vamN0hoMMD7--UCoGbMXwhUMZH9GwCHkbAD3Oxl1TmFIWA3GaqvC4ji7Kt1LM0TPyrffheAhzqPbHSWeHQQzPXVkuBc9iMIuqZ8MkCloByrjDuvWxaGXuE5oz3fGXnktsE8nreJ0699LQRPZTY1hPztD-zmnN) via yfinance Python package
Goal: Analyze soybean futures price trends and volatility to support trading and procurement decisions.
Method:
Daily Returns: Calculated percentage change in price day-to-day to monitor short-term fluctuations and guide risk management.
Moving Averages (7-day & 30-day): Smoothed prices to identify short- and long-term trends, helping traders and procurement teams time purchases and sales strategically.
Volatility (7-day & 30-day): Measured standard deviation of daily returns to assess price risk, inform hedging decisions, and optimize option or futures strategies.
📌 Outcome
Result: Provided a clean, structured dataset with key metrics and visualized price trends, enabling clear insights into market movements.
Relevance: Demonstrates the ability to transform raw market data into actionable information for commodities trading
</details>
---

<details>
    <summary>📊 Finance Institution Transaction EDA
Dataset Source: [Here](https://www.kaggle.com/datasets/abishekhkumar/banking-dataset)
This project analyzes a sample financial transactions dataset to provide branch-level and account-level insights. It demonstrates data validation, outlier detection, and aggregation techniques suitable for both banking data governance and commodities firm analytics.
Key features:
Data completeness check and outlier flagging
Branch-wise transaction counts and debit/credit summaries
Account type balances and currency exposure
Aggregated metrics ready for visualization in Power BI
The dashboard highlights patterns and anomalies, supporting decision-making, monitoring, and reporting.
</details>