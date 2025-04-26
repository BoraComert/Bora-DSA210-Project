import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Read your data
df = pd.read_csv("/Users/boracomert/Desktop/Bora-DSA210-Project-1/merged_output.csv")

# Group function
def group_by_weather(df):
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Classify country temperature
    def classify_country(temp):
        if temp > 20:
            return 'Warm'
        elif temp > 10:
            return 'Moderate'
        else:
            return 'Cold'
    df['Country_Type'] = df['Country_Temp'].apply(classify_country)
    
    # Classify country humidity
    def classify_country_humidity(humidity):
        if humidity < 40:
            return 'Low Humidity'
        elif humidity <= 70:
            return 'Moderate Humidity'
        else:
            return 'High Humidity'
    df['Humidity_Type'] = df['Country_Humidity'].apply(classify_country_humidity)
    
    # Classify country precipitation
    def classify_country_precip(precip):
        if precip < 500:
            return 'Low Precipitation'
        elif precip <= 1000:
            return 'Moderate Precipitation'
        else:
            return 'High Precipitation'
    df['Precipitation_Type'] = df['Country_Precipitation'].apply(classify_country_precip)
    
    # Classify Istanbul humidity
    def classify_istanbul_humidity(humidity):
        if humidity < 40:
            return 'Low Humidity'
        elif humidity <= 70:
            return 'Moderate Humidity'
        else:
            return 'High Humidity'
    df['Istanbul_Humidity_Type'] = df['Avg Humidity (%)'].apply(classify_istanbul_humidity)
    
    return df

# Apply the function
df = group_by_weather(df)

# Group by Istanbul Humidity and Country Humidity
humidity_group = df.groupby(['Istanbul_Humidity_Type', 'Humidity_Type'])['ziyaretci_sayisi'].sum().reset_index()
humidity_pivot = humidity_group.pivot(index='Istanbul_Humidity_Type', columns='Humidity_Type', values='ziyaretci_sayisi').fillna(0)

# Run Chi-Square tests
chi2_hum, p_hum, dof_hum, _ = chi2_contingency(humidity_pivot)
print("\nChi-Square Test between Istanbul Humidity and Country Humidity:")
print(f"Chi2: {chi2_hum:.3f} | p-value: {p_hum:.5f} | dof: {dof_hum}")

# (Optional) Plot humidity
humidity_pivot.plot(kind='bar', figsize=(12,7), width=0.7)
plt.title('Tourist Numbers by Istanbul Humidity and Country Humidity')
plt.ylabel('Total Tourists')
plt.xlabel('Istanbul Humidity Level')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
