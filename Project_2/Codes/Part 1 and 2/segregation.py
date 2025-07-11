import pandas as pd

# Load the CSV file
# Replace 'input_file.csv' with the actual file name
df = pd.read_csv('Nifty 50.csv')

segregated_data = df[['Date', 'Vol.']].copy()  # Explicitly create a copy

# Process the 'Vol.' column to convert it to 'Volume (in Million)'
def process_volume(volume):
    if isinstance(volume, str):
        if volume.endswith('M'):
            return float(volume[:-1])  # Remove 'M' and convert to float
        elif volume.endswith('B'):
            return float(volume[:-1]) * 1e3  # Remove 'B', convert to float, and multiply by 1e3
    return None  # Return None if it doesn't end with 'M' or 'B'

segregated_data['Volume (in Million)'] = segregated_data['Vol.'].apply(process_volume)

# Drop rows with NaN values in the 'Volume (in Million)' column
segregated_data = segregated_data.dropna(subset=['Volume (in Million)'])

# Drop the original 'Vol.' column
segregated_data = segregated_data.drop(columns=['Vol.'])

# Save the segregated data to a new CSV file
# Replace 'output_file.csv' with the desired output file name
segregated_data.to_csv('Final Data1.csv', index=False)