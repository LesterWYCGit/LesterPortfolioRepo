# 🏦 Loan Application Data Validation Project 

This project focuses on validating and cleaning a sample loan application dataset. It demonstrates how raw financial data can be checked for accuracy, completeness, and compliance with regulatory standards. The workflow emphasizes data wrangling, missing value handling, and standardized formatting to prepare the dataset for downstream analysis or decision-making.
---
Source of Data: [Here](https://www.kaggle.com/datasets/bsugiarto9/loan-status-prediction-with-added-nans) 
---
## Key Steps

Data Import

Load raw loan application data using Pandas.

Uniqueness Validation

Verify that all Loan_ID values are unique to prevent duplication errors.

Missing Data Flagging

Flag missing values across all critical fields such as Loan Amount, Credit History, Gender, and others.

Reordering for Review

Reorder the dataset so that complete applications appear at the top and incomplete applications are pushed to the bottom for easier manual or automated review.

Standardization

Standardize categorical fields (such as Gender and Married) for consistent formatting across the dataset.

Export

Export a cleaned dataset in which complete and incomplete applications are clearly separated.

Outputs

cleaned_loan_data.csv
A validated dataset where incomplete applications are flagged and reordered, ready for use in compliance checks, analytics, or model training.
---
# Significance

While no deep analytical insights are derived in this stage, the project highlights the importance of data validation in the financial sector. It ensures that:

Records are accurate and free of duplicates.

Incomplete applications are identifiable and prioritized for follow-up.

Data is standardized for consistency and downstream processing.

This type of workflow is critical for regulatory compliance, audit readiness, and robust data governance in financial institutions.
