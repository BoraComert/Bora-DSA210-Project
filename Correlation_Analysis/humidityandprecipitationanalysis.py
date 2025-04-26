import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/boracomert/Desktop/Bora-DSA210-Project-1/merged_output.csv")

# Grouping function
def group_by_season(df):
    df['Date'] = pd.to_datetime(df['Date'])
    month_to_season = {1: 'Winter', 4: 'Spring', 7: 'Summer', 10: 'Autumn'}
    df['Season'] = df['Date'].dt.month.map(month_to_season)
    
    def classify_country(temp):
        if temp > 20:
            return 'Warm'
        elif temp > 10:
            return 'Moderate'
        else:
            return 'Cold'
    df['Country_Type'] = df['Country_Temp'].apply(classify_country)
    
    # Add Humidity Classificaiton
    def classify_humidity(humidity):
        if humidity < 40:
            return 'Low Humidity'
        elif humidity <= 70:
            return 'Moderate Humidity'
        else:
            return 'High Humidity'
    df['Humidity_Type'] = df['Country_Humidity'].apply(classify_humidity)
    
    # Add Precipitation Type
    def classify_precipitation(precip):
        if precip < 250:
            return 'Low Precipitation'
        elif precip <= 700:
            return 'Moderate Precipitation'
        else:
            return 'High Precipitation'
    df['Precipitation_Type'] = df['Country_Precipitation'].apply(classify_precipitation)
    
    return df

df = group_by_season(df)

# 4. Pivot tables
# a) Temperature (already done previously)
temp_group = df.groupby(['Season', 'Country_Type'])['ziyaretci_sayisi'].sum().reset_index()
temp_pivot = temp_group.pivot(index='Season', columns='Country_Type', values='ziyaretci_sayisi').fillna(0)

# b) Humidity
humidity_group = df.groupby(['Season', 'Humidity_Type'])['ziyaretci_sayisi'].sum().reset_index()
humidity_pivot = humidity_group.pivot(index='Season', columns='Humidity_Type', values='ziyaretci_sayisi').fillna(0)

# c) Precipitation
precip_group = df.groupby(['Season', 'Precipitation_Type'])['ziyaretci_sayisi'].sum().reset_index()
precip_pivot = precip_group.pivot(index='Season', columns='Precipitation_Type', values='ziyaretci_sayisi').fillna(0)

# 5. Chi-Square Tests
# a) Temperature Chi-Square
chi2_temp, p_temp, dof_temp, _ = chi2_contingency(temp_pivot)
print("\nTemperature Chi-Square Test:")
print(f"Chi2: {chi2_temp:.3f} | p-value: {p_temp:.5f} | dof: {dof_temp}")

# b) Humidity Chi-Square
chi2_hum, p_hum, dof_hum, _ = chi2_contingency(humidity_pivot)
print("\nHumidity Chi-Square Test:")
print(f"Chi2: {chi2_hum:.3f} | p-value: {p_hum:.5f} | dof: {dof_hum}")

# c) Precipitation Chi-Square
chi2_prec, p_prec, dof_prec, _ = chi2_contingency(precip_pivot)
print("\nPrecipitation Chi-Square Test:")
print(f"Chi2: {chi2_prec:.3f} | p-value: {p_prec:.5f} | dof: {dof_prec}")

# Plot for Humidity
humidity_pivot.plot(kind='bar', figsize=(12,7), width=0.7)
plt.title('Tourist Numbers by Season and Country Climate (Humidity)')
plt.ylabel('Total Tourists')
plt.xlabel('Season')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Plot for Precipitation
precip_pivot.plot(kind='bar', figsize=(12,7), width=0.7)
plt.title('Tourist Numbers by Season and Country Climate (Precipitation)')
plt.ylabel('Total Tourists')
plt.xlabel('Season')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
