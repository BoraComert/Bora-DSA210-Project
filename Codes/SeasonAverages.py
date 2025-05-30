import pandas as pd

# File paths
input_file = 'monthly_totals_2019-2024 .csv'         
output_file = 'seasonal_averages.csv'   

# Load the CSV data
df = pd.read_csv(input_file)
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m')
df.set_index('Date', inplace=True)

# Resample into 3-month (quarterly) periods starting from January
seasonal_means = df.resample('Q').mean()

# Rename the index to the starting month of the quarter (e.g., '2019-01')
seasonal_means.index = [i.to_timestamp(how='start').strftime('%Y-%m') for i in seasonal_means.index.to_period('Q')]

# Reset index and rename column
seasonal_means.reset_index(inplace=True)
seasonal_means.rename(columns={'index': 'Season'}, inplace=True)

# Save to new CSV
seasonal_means.to_csv(output_file, index=False)

print(f"Seasonal averages saved to '{output_file}'")
