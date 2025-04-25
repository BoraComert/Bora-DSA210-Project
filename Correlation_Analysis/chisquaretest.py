import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Read your dataset
df = pd.read_csv("/Users/boracomert/Desktop/Bora-DSA210-Project-1/merged_output.csv")

# Grouping function , groups tourists from hot countries, medium countries and cold countries.
def group_by_season(df):
    """
    Adds 'Season' and 'Country_Type' columns based on Date and Country_Temp.
    """
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Map months to seasons
    month_to_season = {
        1: 'Winter',
        4: 'Spring',
        7: 'Summer',
        10: 'Autumn'
    }
    df['Season'] = df['Date'].dt.month.map(month_to_season)
    
    # Classify countries by average temperature
    def classify_country(temp):
        if temp > 20:
            return 'Warm'
        elif temp > 10:
            return 'Moderate'
        else:
            return 'Cold'
    
    df['Country_Type'] = df['Country_Temp'].apply(classify_country)
    
    return df


df = group_by_season(df)

# Create pivot table
season_country_group = df.groupby(['Season', 'Country_Type'])['ziyaretci_sayisi'].sum().reset_index()

pivot_table = season_country_group.pivot(index='Season', columns='Country_Type', values='ziyaretci_sayisi')

pivot_table = pivot_table.fillna(0)

print("Pivot Table (Tourists by Season and Country Type):")
print(pivot_table)

# 5. Run Chi-Square Test
chi2, p, dof, expected = chi2_contingency(pivot_table)

print("\nChi-Square Test Results:")
print(f"Chi2 statistic: {chi2:.3f}")
print(f"P-value: {p:.5f}")
print(f"Degrees of freedom: {dof}")
