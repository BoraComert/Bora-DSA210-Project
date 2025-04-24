import pandas as pd

# Load data
istanbul_weather = pd.read_csv('/Users/boracomert/Desktop/Bora-DSA210-Project-1/seasonal averages/istanbul_seasonal_averages.csv')
country_temps = pd.read_csv('/Users/boracomert/Desktop/Bora-DSA210-Project-1/seasonal averages/filtered_climate_data_temp.csv')
country_pr = pd.read_csv('/Users/boracomert/Desktop/Bora-DSA210-Project-1/seasonal averages/filtered_climate_pr_data.csv')

# Convert date columns to datetime
istanbul_weather['Date'] = pd.to_datetime(istanbul_weather['Date'])
country_temps['Date'] = pd.to_datetime(country_temps['Date'])
country_pr['Date'] = pd.to_datetime(country_pr['Date'])

# Melt country temperature data (wide to long format)
melted = country_temps.melt(id_vars='Date', var_name='Country', value_name='Country_Temp')

# Melt precipitation data (wide to long format)
melted_pr = country_pr.melt(id_vars='Date', var_name='Country', value_name='Country_Precipitation')

# Merge the temperature and precipitation data with Istanbul weather data
merged_temp = pd.merge(melted, istanbul_weather, on='Date', how='left')
final_merged = pd.merge(merged_temp, melted_pr, on=['Date', 'Country'], how='left')

# Reorganize columns to have Country_Temp and Country_Precipitation together
final_merged = final_merged[['Date', 'Country', 'Country_Temp', 'Country_Precipitation', 'Avg Temperature (C)', 'Avg Humidity (%)', 'Total Precipitation (mm)']]

# Save the final merged DataFrame to a new CSV file
final_merged.to_csv('/Users/boracomert/Desktop/Bora-DSA210-Project-1/seasonal averages/final_weather_with_precipitation.csv', index=False)

# Optionally, print the final merged DataFrame
print(final_merged)
