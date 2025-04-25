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


season_country_group = df.groupby(['Season', 'Country_Type'])['ziyaretci_sayisi'].sum().reset_index()

#Pivot the table to make it easier to see
pivot_table = season_country_group.pivot(index='Season', columns='Country_Type', values='ziyaretci_sayisi')

pivot_table = pivot_table.fillna(0)


print(pivot_table)

pivot_table.plot(kind='bar', figsize=(10, 6))
plt.title('Tourist Numbers by the Season of Istanbul and Origin Country Condition')
plt.ylabel('Total Tourists')
plt.xlabel('Season of Istanbul')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
