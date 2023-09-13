# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('loan.csv')

# Display basic information about the dataset
print(data.info())

# Summary statistics
print(data.describe())

# Univariate Analysis
# Example: Histogram of loan amounts
plt.figure(figsize=(8, 6))
sns.histplot(data['loan_amnt'], bins=20, kde=True)
plt.title('Distribution of Loan Amount')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()

# Bivariate Analysis
# Example: Scatter plot of loan amount vs. income
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='annual_inc', y='loan_amnt', hue='loan_status')
plt.title('Loan Amount vs. Income')
plt.xlabel('Income')
plt.ylabel('Loan Amount')
plt.show()
