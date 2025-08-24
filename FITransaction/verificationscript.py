import pandas as pd

# Step 1: Import dataset
df = pd.read_excel('FITransaction/banking_dataset.xlsx')

# Step 2: Verify completeness
print("Missing values per column:\n", df.isnull().sum())

# Step 3: Flag outliers
df['Outlier_Transaction'] = df['Transaction Amount'] > 5000
df['Outlier_Balance'] = df['Account Balance'] > 100000

# Extra: review flagged rows
outliers = df[df['Outlier_Transaction'] | df['Outlier_Balance']]
print("Flagged outliers:\n", outliers)

# Step 4: Save verified dataset
df.to_excel('FITransaction/verified_transactions.xlsx', index=False)
print("Verified dataset saved to FITransaction/verified_transactions.xlsx")
