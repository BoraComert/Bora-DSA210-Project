import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
df = pd.read_csv("/Users/boracomert/Desktop/Bora-DSA210-Project-1/merged_output.csv")

# Classify Istanbul Precipitation
def classify_istanbul_precip(precip):
    if precip < 50:
        return 'Low'
    elif precip <= 100:
        return 'Medium'
    else:
        return 'High'

# Classify Country Precipitation
def classify_country_precip(precip):
    if precip < 500:
        return 'Low Precipitation'
    elif precip <= 1000:
        return 'Moderate Precipitation'
    else:
        return 'High Precipitation'

# Apply the classifications
df['Istanbul_Precip_Type'] = df['Total Precipitation (mm)'].apply(classify_istanbul_precip)
df['Precipitation_Type'] = df['Country_Precipitation'].apply(classify_country_precip)

# Create pivot table: Istanbul Precip Type (rows) vs Country Precip Type (columns)
pivot_precip = df.groupby(['Istanbul_Precip_Type', 'Precipitation_Type'])['ziyaretci_sayisi'].sum().unstack().fillna(0)

# Reorder for cleaner visuals
pivot_precip = pivot_precip.reindex(index=['Low', 'Medium', 'High'],
                                     columns=['Low Precipitation', 'Moderate Precipitation', 'High Precipitation'])

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_precip, annot=True, fmt=".0f", cmap="YlGnBu", cbar_kws={'label': 'Number of Tourists'})
plt.title("Tourists by Istanbul vs. Country Precipitation Levels")
plt.xlabel("Country Precipitation Level")
plt.ylabel("Istanbul Precipitation Level")
plt.tight_layout()
plt.show()
