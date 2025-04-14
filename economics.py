import pandas as pd

# Load the dataset with a custom User-Agent to avoid 403 error
url = "https://ourworldindata.org/grapher/daily-median-income.csv?v=1&csvType=full&useColumnShortNames=true"
df = pd.read_csv(url, storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})

# Filter for Turkey
turkey_df = df[df['Entity'] == 'United States']

# Filter for the years 2019–2024
turkey_df = turkey_df[(turkey_df['Year'] >= 2019) & (turkey_df['Year'] <= 2024)]

# Reset index for cleanliness
turkey_df.reset_index(drop=True, inplace=True)

# Show the result
print(turkey_df)
