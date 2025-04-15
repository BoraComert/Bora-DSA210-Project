import pandas as pd
import requests
import matplotlib.pyplot as plt

# Step 1: Load the CSV data
df = pd.read_csv(
    "https://ourworldindata.org/grapher/inflation-of-consumer-prices.csv?v=1&csvType=full&useColumnShortNames=true",
    storage_options={'User-Agent': 'Our World In Data data fetch/1.0'}
)

# Step 2: Load the metadata (optional, useful for descriptions/units)
metadata = requests.get(
    "https://ourworldindata.org/grapher/inflation-of-consumer-prices.metadata.json?v=1&csvType=full&useColumnShortNames=true"
).json()

# Step 3: Filter the data for Turkey
turkey_df = df[df['Entity'] == 'Turkey']

# Step 4: Sort by year just in case
turkey_df = turkey_df.sort_values(by='Year')

# Step 5: Plot inflation over time
plt.figure(figsize=(10, 5))
plt.plot(turkey_df['Year'], turkey_df['Inflation of consumer prices (annual %)'], marker='o', linestyle='-')
plt.title("Inflation in Turkey (Consumer Prices, Annual %)")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
