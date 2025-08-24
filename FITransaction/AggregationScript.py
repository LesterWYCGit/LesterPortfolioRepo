import pandas as pd

# Step 1: Load verified dataset
df = pd.read_excel('FITransaction/verified_transactions.xlsx')

# --- 1️⃣ Total transaction count per branch ---
branch_count = df.groupby('Branch')['Transaction Type'].count().reset_index()
branch_count.rename(columns={'Transaction Type': 'Transaction_Count'}, inplace=True)

# --- 2️⃣ Account type total balance (filterable by currency in Power BI) ---
balance_summary = df.groupby(['Account Type', 'Currency'])['Account Balance'].sum().reset_index()
balance_summary.rename(columns={'Account Balance': 'Total_Balance'}, inplace=True)

# --- 3️⃣ Total debit and credit per branch ---
branch_debit_credit = df.pivot_table(
    index='Branch',
    columns='Transaction Type',
    values='Transaction Amount',
    aggfunc='sum',
    fill_value=0
).reset_index()

# --- 4️⃣ Balance summary per account type (min, max, avg) ---
balance_stats = df.groupby('Account Type')['Account Balance'].agg(['min', 'max', 'mean']).reset_index()
balance_stats.rename(columns={'min':'Min_Balance','max':'Max_Balance','mean':'Avg_Balance'}, inplace=True)

# Step 2: Save all 4 outputs into one Excel for Power BI
with pd.ExcelWriter('FITransaction/aggregated_for_PowerBI.xlsx') as writer:
    branch_count.to_excel(writer, sheet_name='Branch_Transaction_Count', index=False)
    balance_summary.to_excel(writer, sheet_name='AccountType_Balance', index=False)
    branch_debit_credit.to_excel(writer, sheet_name='Branch_Debit_Credit', index=False)
    balance_stats.to_excel(writer, sheet_name='Balance_Stats', index=False)

print("Aggregated data for Power BI saved to FITransaction/aggregated_for_PowerBI.xlsx")
