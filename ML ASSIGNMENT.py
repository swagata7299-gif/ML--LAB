import numpy as np
import pandas as pd

# Load the data from the worksheet
data = {
    'Customer': ['C_1', 'C_2', 'C_3', 'C_4', 'C_5', 'C_6', 'C_7', 'C_8', 'C_9', 'C_10'],
    'Candies (#)': [20, 16, 27, 19, 24, 22, 15, 18, 21, 16],
    'Mangoes (Kg)': [6, 3, 6, 1, 4, 1, 4, 4, 1, 2],
    'Milk Packets (#)': [2, 6, 2, 2, 2, 5, 2, 2, 4, 4],
    'Payment (Rs)': [386, 289, 393, 110, 280, 167, 271, 274, 148, 198]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Segregate the data into matrices A (features) and C (target)
A = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values
C = df['Payment (Rs)'].values

# Part 1: What is the dimensionality of the vector space for this data?
dimensionality = A.shape[1]
print(f"Dimensionality of the vector space: {dimensionality}")

# Part 2: How many vectors exist in this vector space?
num_vectors = A.shape[0]
print(f"Number of vectors in the vector space: {num_vectors}")

# Part 3: What is the rank of Matrix A?
rank_A = np.linalg.matrix_rank(A)
print(f"Rank of Matrix A: {rank_A}")

# Part 4: Using Pseudo-Inverse to find the cost of each product
A_pseudo_inverse = np.linalg.pinv(A)
X = np.dot(A_pseudo_inverse, C)
print(f"Cost of each product (candies, mangoes, milk packets): {X}")

# Part 5: Calculate the model vector X for predicting the cost of the products
predicted_C = np.dot(A, X)
print(f"Predicted payments: {predicted_C}")
