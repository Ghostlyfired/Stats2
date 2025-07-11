import pandas as pd

# Load the dataset
data = pd.read_csv('Final Data1.csv')

# Check for NaN values
nan_count = data.isna().sum()

# Check for negative values in the 'Volume (in Million)' column
neg_count = (data['Volume (in Million)'] <= 0).sum()

# Print the results
print(f"NaN values in each column:\n{nan_count}")
print(f"Number of non positive values in 'Volume (in Million)': {neg_count}")