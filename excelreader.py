import pandas as pd

# Load Excel data
df = pd.read_excel("allprecipatation.xlsx")

# Confirm actual column name for 'code' — update if needed
df = df.set_index("code")

# Keep only country-level data (exclude anything with a dot in the code)
df = df[~df.index.str.contains(r"\.")]

# Select columns 17 to 40 (Python index 16 to 41)
df_filtered = df.iloc[:, 16:41]

# Transpose to get dates as rows
df_transposed = df_filtered.T
df_transposed.index.name = "Date"

# Save as CSV
df_transposed.to_csv("filtered_climate_data.csv")

print("Saved filtered data with only country averages to 'filtered_climate_data.csv'")
