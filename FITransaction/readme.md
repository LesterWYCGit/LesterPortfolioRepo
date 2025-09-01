# 📊 Finance Institution Transaction EDA

This project analyzes a sample financial transactions dataset to provide branch-level and account-level insights. It demonstrates data validation, outlier detection, and aggregation techniques suitable for both banking data governance and commodities firm analytics.
---
📌 Source of Data: [Here](https://www.kaggle.com/datasets/abishekhkumar/banking-dataset) 
---
## The workflow consists of two main steps:

Data validation and outlier flagging

Data aggregation and preparation for Power BI dashboards

Features

Data Validation & Outlier Detection
Completeness check for missing values
Outlier flagging for:
Transaction Amounts greater than 5,000
Account Balances greater than 100,000
Verified dataset saved with additional columns for flagged records
Aggregation for Power BI
Branch-level transaction counts
Debit and credit totals per branch
Account type balances with currency exposure
Balance statistics (minimum, maximum, average) per account type

Aggregated metrics saved into a single Excel file with multiple sheets for direct Power BI import

---
## Aggregated Excel File Sheets

Branch_Transaction_Count: 
Groups by Branch, counts how many transactions per branch.Useful for branch performance monitoring.

AccountType_Balance:
Groups by Account Type + Currency, sums balances.

Branch_Debit_Credit:
Pivot table showing total debit and total credit per branch.

Balance_Stats:
Min, Max, and Average balances. Useful for risk & customer segmentation (e.g., high-value vs low-value accounts).

---
## Future Enhancements

Export flagged outliers to a separate Excel file for audit purposes
Add statistical outlier detection (z-scores or IQR method)
Include time-based aggregations (monthly transaction counts, balance trends)
Generate visualizations (histograms, boxplots) directly in Python
Connect directly to Power BI for real-time dashboards
