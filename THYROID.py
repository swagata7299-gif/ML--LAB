
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load the data (replace 'your_file.xlsx' with the actual file path)
# df = pd.read_excel('your_file.xlsx', sheet_name='thyroid0387_UCI')

# Sample DataFrame for illustration (as actual data isn't provided)
# Replace this with the actual data loading step.
data = {
    'Age': [25, 30, np.nan, 35, 45, 50, 60, 70, 80, 90],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'TSH': [1.3, 2.5, 0.9, np.nan, 4.5, 2.7, 1.8, 3.2, 2.9, 1.7],
    'T3': [1.1, 1.5, 0.8, 1.2, 1.3, np.nan, 1.4, 1.6, 1.7, 1.8],
    'Class': ['normal', 'hyperthyroid', 'hypothyroid', 'normal', 'normal', 'hyperthyroid', 'hypothyroid', 'normal', 'hyperthyroid', 'hypothyroid']
}
df = pd.DataFrame(data)

# Part 1: Study each attribute and associated values, identify the datatype
print("Data Types:")
print(df.dtypes)
print("\n")

# Part 2: Encoding categorical attributes
# Identify categorical variables
categorical_vars = df.select_dtypes(include=['object']).columns
print("Categorical Variables:", categorical_vars)

# Example encoding scheme: Label Encoding for ordinal, One-Hot Encoding for nominal
# Gender is nominal, Class is ordinal (depending on domain knowledge)
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])

# For One-Hot Encoding (example)
df = pd.get_dummies(df, columns=['Class'])

print("\nData after encoding:")
print(df.head())
print("\n")

# Part 3: Study the data range for numeric variables
numeric_vars = df.select_dtypes(include=[np.number]).columns
print("Data Range for Numeric Variables:")
for var in numeric_vars:
    print(f"{var}: Min = {df[var].min()}, Max = {df[var].max()}")

# Part 4: Study the presence of missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handling missing values (example: filling with mean)
df.fillna(df.mean(), inplace=True)

print("\nData after handling missing values:")
print(df.head())

# Part 5: Study presence of outliers
print("\nOutliers Detection (using IQR method):")
for var in numeric_vars:
    Q1 = df[var].quantile(0.25)
    Q3 = df[var].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[var] < lower_bound) | (df[var] > upper_bound)]
    print(f"{var}: {len(outliers)} outliers")
    sns.boxplot(x=df[var])
    plt.title(f"Boxplot for {var}")
    plt.show()

# Part 6: Calculate the mean and variance (or standard deviation) for numeric variables
print("\nMean and Variance for Numeric Variables:")
for var in numeric_vars:
    mean_val = df[var].mean()
    variance_val = df[var].var()
    std_dev_val = df[var].std()
    print(f"{var}: Mean = {mean_val}, Variance = {variance_val}, Standard Deviation = {std_dev_val}")

