import pandas as pd

#I used this code to merge tourist data with countries and istanbul's seasonal weather data


df1 = pd.read_csv('/Users/boracomert/Desktop/Bora-DSA210-Project-1/seasonal averages/final_weather_with_precipitation_and_humidity.csv')  # Replace with your actual file name
df2 = pd.read_csv('seasonal_tourist_data.csv')  

df1['Date'] = df1['Date'].str.strip()  # For weather data
df2['Date'] = df2['Date'].str.strip()  # For tourist data

# Convert 'Date' in df2 (tourist data) to datetime, adding '-01' to make it the first day of the month
df2['Date'] = pd.to_datetime(df2['Date'] + '-01', errors='coerce')  # Add '-01' to make it 'YYYY-MM-01'

# Convert 'Date' in df1 (weather data) to datetime, if its not already
df1['Date'] = pd.to_datetime(df1['Date'], errors='coerce')

# Check the data types after conversion
print(f"\ndf1 'Date' type after conversion: {df1['Date'].dtype}")
print(f"df2 'Date' type after conversion: {df2['Date'].dtype}")

# Merge datasets based on vCountryvand Date and drop column with 0
merged_df = pd.merge(df1, df2[['Country', 'Date', 'ziyaretci_sayisi']], on=['Country', 'Date'], how='left')

merged_df['ziyaretci_sayisi'].fillna(0, inplace=True)


merged_df.to_csv('merged_file.csv', index=False)
print("Merged file has been saved as 'merged_file.csv'.")