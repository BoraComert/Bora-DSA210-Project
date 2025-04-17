import pandas as pd

def get_turkey_medianIncome(filepath):
    # Load the CSV file
    df = pd.read_csv(filepath)

    # Filter for Turkey and years between 2019 and 2024 
    turkey_df = df[
        (df['Entity'] == 'Turkey') &
        (df['Year'] >= 2019) &
        (df['Year'] <= 2024)
    ]

    return turkey_df


turkey_inflation = get_turkey_medianIncome("daily-median-income.csv")
print(turkey_inflation[['Year', 'Median income or consumption']])

turkey_inflation.to_csv("turkey_medianIncome_2019_2024.csv", index=False)


print("Saved to turkey_MedianIncome_2019_2024.csv")