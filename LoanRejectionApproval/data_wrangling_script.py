
# Step 1: Importing libraries & dataset, then Validate unique loan id 

import pandas as pd

data = pd.read_csv('LoanRejectionApproval/rawdata_loan.csv')

if data['Loan_ID'].duplicated().sum() == 0:
    print("All Loan_IDs are unique")
else:
    print("Warning: Duplicate Loan_IDs found!")

# Step 2: Flag missing critical fields and Reorder dataset 
#         Incomplete rows to the bottom

critical_cols = [
    'Loan_ID', 'Gender', 'Married', 'Dependents', 
    'Education', 'Self_Employed', 'ApplicantIncome', 
    'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 
    'Credit_History', 'Property_Area', 'Loan_Status'
]

for col in data.columns:
    data[col + '_missing'] = data[col].isnull()

# Rearrange rows: complete first, incomplete last
missing_flags = [col for col in data.columns if col.endswith('_missing')]
complete_rows = data[~data[missing_flags].any(axis=1)]
incomplete_rows = data[data[missing_flags].any(axis=1)]
data_sorted = pd.concat([complete_rows, incomplete_rows])


# Step 3: Standardize categorical columns for consistency (Foolproof)
data_sorted['Gender'] = data_sorted['Gender'].str.capitalize()
data_sorted['Married'] = data_sorted['Married'].str.capitalize()

# Drop the helper columns before exporting
data_cleaned = data_sorted.drop(columns=missing_flags)

# Step 4: Export cleaned & flagged dataset
data_cleaned.to_csv('LoanRejectionApproval/cleaned_loan_data.csv', index=False)
print(f"Exported cleaned file with {len(complete_rows)} complete and {len(incomplete_rows)} incomplete applications.")