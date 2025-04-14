import pandas as pd

# URLs to the datasets
income_url = "https://ourworldindata.org/grapher/daily-median-income.csv"
gdp_url = "https://ourworldindata.org/grapher/gdp-per-capita-worldbank.csv"
inflation_url = "https://ourworldindata.org/grapher/inflation-of-consumer-prices.csv"

# Load datasets
income_df = pd.read_csv(income_url)
gdp_df = pd.read_csv(gdp_url)
inflation_df = pd.read_csv(inflation_url)

# Filter function for a given year range
def filter_years(df, start=2019, end=2024):
    return df[(df['Year'] >= start) & (df['Year'] <= end)]

# Filter by years 2019–2024
income_filtered = filter_years(income_df)
gdp_filtered = filter_years(gdp_df)
inflation_filtered = filter_years(inflation_df)

# Filter by country (Turkey)
income_turkey = income_filtered[income_filtered['Entity'] == 'Turkey']
gdp_turkey = gdp_filtered[gdp_filtered['Entity'] == 'Turkey']
inflation_turkey = inflation_filtered[inflation_filtered['Entity'] == 'Turkey']

# Print sample data
print("Daily Median Income (Turkey, 2019–2024):")
print(income_turkey.head(), "\n")

print("GDP per Capita (Turkey, 2019–2024):")
print(gdp_turkey.head(), "\n")

print("Inflation (Turkey, 2019–2024):")
print(inflation_turkey.head(), "\n")
