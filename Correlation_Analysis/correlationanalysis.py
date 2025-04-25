import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import pearsonr

def group_by_season(df):
    """
    Takes a DataFrame with 'Date' and 'Country_Temp',
    and adds 'Season' and 'Country_Type' columns.
    """
    # Convert Date to datetime if not already
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Map seasons based on the month (only 1, 4, 7, 10 exist)
    month_to_season = {
        1: 'Winter',
        4: 'Spring',
        7: 'Summer',
        10: 'Autumn'
    }
    df['Season'] = df['Date'].dt.month.map(month_to_season)
    
    # Countries will be classified in accordance with their temperatures
    def classify_country(temp):
        if temp > 20:
            return 'Warm'
        elif temp > 10:
            return 'Moderate'
        else:
            return 'Cold'

    df['Country_Type'] = df['Country_Temp'].apply(classify_country)
    
    return df

seasons_df = pd.read_csv("/Users/boracomert/Desktop/Bora-DSA210-Project-1/merged_output.csv")

df = group_by_season(seasons_df)

clean_df = df.dropna(subset=['Country_Temp', 'ziyaretci_sayisi'])

# Calculate Pearson correlation
corr, p_value = pearsonr(clean_df['Country_Temp'], clean_df['ziyaretci_sayisi'])

print(f"Pearson correlation: {corr:.3f}")
print(f"P-value: {p_value:.3f}")