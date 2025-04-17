import pandas as pd

# Load both CSV files
weather_df = pd.read_csv("monthly_totals_2019.csv")
tourists_df = pd.read_csv("turkiye-ve-istanbul-olceginde-gelen-yabanci-ziyaretci-sayisi.csv")

# Convert date columns
weather_df['Date'] = pd.to_datetime(weather_df['Date'], format='%Y-%m')
tourists_df['tarih'] = pd.to_datetime(tourists_df['tarih'])

# Filter only Istanbul data
istanbul_df = tourists_df[tourists_df['istanbul_turkiye'] == 'İstanbul'].copy()

# Add Year-Month for grouping
istanbul_df['YearMonth'] = istanbul_df['tarih'].dt.to_period('M')

# Group by Year-Month and sum visitor numbers
monthly_visitors = istanbul_df.groupby('YearMonth')['ziyaretci_sayisi'].sum().reset_index()

# Convert to datetime for merging
monthly_visitors['Date'] = monthly_visitors['YearMonth'].dt.to_timestamp()

# Merge with weather data
merged_df = pd.merge(weather_df, monthly_visitors[['Date', 'ziyaretci_sayisi']], on='Date', how='left')

# Optional: Rename for clarity
merged_df.rename(columns={'ziyaretci_sayisi': 'Monthly Tourists'}, inplace=True)

# Save to new CSV
merged_df.to_csv("weather_with_istanbul_tourists.csv", index=False)
