import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the worksheet (assuming the file is named 'Lab Session Data.xlsx')
# Since we don't have access to the actual Excel file, replace 'your_file.xlsx' with the actual file path.
# df = pd.read_excel('your_file.xlsx', sheet_name='IRCTC Stock Price')

# Sample DataFrame for illustration
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Price': np.random.normal(700, 50, 100),  # Random prices around 700 with a std deviation of 50
    'Chg%': np.random.normal(0, 2, 100)  # Random percentage change around 0 with a std deviation of 2%
}
df = pd.DataFrame(data)

# Convert Date to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Part 1: Calculate the mean and variance of the Price data
price_mean = statistics.mean(df['Price'])
price_variance = statistics.variance(df['Price'])
print(f"Mean of Price data: {price_mean}")
print(f"Variance of Price data: {price_variance}")

# Part 2: Select the price data for all Wednesdays and calculate the sample mean
wednesdays = df[df['Date'].dt.weekday == 2]  # 2 corresponds to Wednesday
wednesday_mean = statistics.mean(wednesdays['Price'])
print(f"Sample mean for Wednesdays: {wednesday_mean}")
print(f"Comparison: Wednesday mean vs Population mean: {wednesday_mean} vs {price_mean}")

# Part 3: Select the price data for the month of April and calculate the sample mean
april_data = df[df['Date'].dt.month == 4]
april_mean = statistics.mean(april_data['Price'])
print(f"Sample mean for April: {april_mean}")
print(f"Comparison: April mean vs Population mean: {april_mean} vs {price_mean}")

# Part 4: Find the probability of making a loss over the stock (Chg% < 0)
loss_probability = len(df[df['Chg%'] < 0]) / len(df)
print(f"Probability of making a loss: {loss_probability}")

# Part 5: Calculate the probability of making a profit on Wednesday (Chg% > 0 on Wednesdays)
wednesday_profit_probability = len(wednesdays[wednesdays['Chg%'] > 0]) / len(wednesdays)
print(f"Probability of making a profit on Wednesday: {wednesday_profit_probability}")

# Part 6: Calculate the conditional probability of making profit, given that today is Wednesday
conditional_profit_probability = (wednesday_profit_probability * len(wednesdays)) / len(df[df['Chg%'] > 0])
print(f"Conditional probability of making a profit given it's Wednesday: {conditional_profit_probability}")

# Part 7: Scatter plot of Chg% data against the day of the week
df['DayOfWeek'] = df['Date'].dt.day_name()
plt.scatter(df['DayOfWeek'], df['Chg%'])
plt.title('Scatter Plot of Chg% vs Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Chg%')
plt.show()
