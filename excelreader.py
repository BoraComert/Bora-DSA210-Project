import pandas as pd

# Load Excel data
df = pd.read_excel("seasonal_climate_data.xlsx")

# Filter to only 'Country Average' rows
df_country = df[df["Type"] == "Country Average"]

# Set 'Code' or 'Name' as index if needed
df_country = df_country.set_index("Code") 

# Drop non-date columns (keeping only seasonal dates)
date_columns = [col for col in df_country.columns if col[:4].isdigit() and "-" in col]
df_filtered = df_country[date_columns]

# Change the place of the row and columns to fit the existing data sets
df_transposed = df_filtered.T
df_transposed.index.name = "Date"

# Save as a new CSV file
df_transposed.to_csv("filtered_climate_data.csv")

print("Filtered climate data saved to 'filtered_climate_data.csv'")
