
# Step 1: Importing libraries & dataset, then Validate unique loan id 

import pandas as pd

data = pd.read_csv('rawdata_loan.csv')

if data['Loan_ID'].duplicated().sum() == 0:
    print("All Loan_IDs are unique")
else:
    print("Warning: Duplicate Loan_IDs found!")

# Step 2: Flag missing critical fields and Reorder dataset 
#         Incomplete rows to the bottom

critical_cols = ['LoanAmount', 'ApplicantIncome', 'Credit_History']
for col in critical_cols:
    data[col + '_missing'] = data[col].isnull()

complete_rows = data[~data[[col + '_missing' for col in critical_cols]].any(axis=1)]
incomplete_rows = data[data[[col + '_missing' for col in critical_cols]].any(axis=1)]
data_sorted = pd.concat([complete_rows, incomplete_rows])

# Step 3: Standardize categorical columns for consistency
data_sorted['Gender'] = data_sorted['Gender'].str.capitalize()
data_sorted['Married'] = data_sorted['Married'].str.capitalize()

# Step 4: Export cleaned & flagged dataset
data_sorted.to_csv('cleaned_loan_data.csv', index=False)
print("Cleaned dataset exported as 'cleaned_loan_data.csv'")