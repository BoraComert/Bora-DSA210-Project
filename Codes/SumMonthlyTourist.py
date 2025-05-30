import pandas as pd

#I used this code to create a seasonal tourist table from monthly tourist numbers

# Read the CSV file
df = pd.read_csv("milliyetlerine-gore-istanbul-a-gelen-yabanci-turist-sayisi.csv")

# Convert 'tarih' column to datetime
df['tarih'] = pd.to_datetime(df['tarih'])

# Create a new column every season
df['date'] = df['tarih'].dt.to_period('Q').dt.start_time

# Group each nationality
grouped = df.groupby(['uyruk', 'date'])['ziyaretci_sayisi'].sum().reset_index()

# Format the date as YYYY-MM
grouped['date'] = grouped['date'].dt.strftime('%Y-%m')
# Reorder columns so the date is first
grouped = grouped[['date', 'uyruk', 'ziyaretci_sayisi']]

# Save to CSV
grouped.to_csv("quarterly_visitors_by_country.csv", index=False)
