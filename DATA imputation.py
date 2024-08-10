import pandas as pd
import numpy as np
import seaborn as sns

# Load the data (replace 'your_file.xlsx' with the actual file path)
# df = pd.read_excel('your_file.xlsx', sheet_name='thyroid0387_UCI')

# Sample DataFrame for illustration (as actual data isn't provided)
data = {
    'Age': [25, 30, np.nan, 35, 45, 50, 60, 70, 80, 90],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', np.nan],
    'TSH': [1.3, 2.5, 0.9, np.nan, 4.5, 2.7, 1.8, 3.2, 2.9, 1.7],
    'T3': [1.1, 1.5, 0.8, 1.2, 1.3, np.nan, 1.4, 1.6, 1.7, 1.8],
    'Class': ['normal', 'hyperthyroid', 'hypothyroid', 'normal', 'normal', 'hyperthyroid', 'hypothyroid', 'normal', 'hyperthyroid', 'hypothyroid']
}
df = pd.DataFrame(data)

# Part 1: Detect and impute missing values for numeric variables based on the presence of outliers

# Step 1: Identify numeric columns
numeric_vars = df.select_dtypes(include=[np.number]).columns

# Step 2: Check for outliers using the IQR method and decide on imputation strategy
for var in numeric_vars:
    Q1 = df[var].quantile(0.25)
    Q3 = df[var].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[var] < lower_bound) | (df[var] > upper_bound)]
    
    if len(outliers) > 0:
        # If outliers are present, use the median for imputation
        imputation_value = df[var].median()
        df[var].fillna(imputation_value, inplace=True)
        print(f"Imputed missing values in {var} with median: {imputation_value}")
    else:
        # If no outliers, use the mean for imputation
        imputation_value = df[var].mean()
        df[var].fillna(imputation_value, inplace=True)
        print(f"Imputed missing values in {var} with mean: {imputation_value}")

# Part 2: Impute missing values for categorical variables using the mode
categorical_vars = df.select_dtypes(include=['object']).columns

for var in categorical_vars:
    mode_value = df[var].mode()[0]  # Mode returns a series, so take the first element
    df[var].fillna(mode_value, inplace=True)
    print(f"Imputed missing values in {var} with mode: {mode_value}")

# Display the DataFrame after imputation
print("\nDataFrame after imputation:")
print(df)



