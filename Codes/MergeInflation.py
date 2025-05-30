import pandas as pd

#I used this code to merge tourist data with inflation data

# Load both datasets
visitors_df = pd.read_csv('turkiye-ve-istanbul-olceginde-gelen-yabanci-ziyaretci-sayisi.csv')
inflation_df = pd.read_csv('yoy_inflation.csv')

# Filter only rows for Istanbul
visitors_df = visitors_df[visitors_df['istanbul_turkiye'] == 'İstanbul']


# Convert 'tarih' to datetime
visitors_df['tarih'] = pd.to_datetime(visitors_df['tarih'])

# Create 'year_month' column for merging
visitors_df['year_month'] = visitors_df['tarih'].dt.to_period('M').astype(str)

# Filter years 2019 to 2024
visitors_df = visitors_df[visitors_df['tarih'].dt.year.between(2019, 2024)]

# Rename 'Month' in inflation data to match for merging
inflation_df.rename(columns={'Month': 'year_month'}, inplace=True)

# Merge the two datasets on 'year_month'
merged_df = pd.merge(
    visitors_df[['year_month', 'ziyaretci_sayisi']],
    inflation_df[['year_month', 'YoY_Inflation (%)']],
    on='year_month',
    how='inner'
)

merged_df = merged_df.sort_values(by='year_month')

# Save the merged data to a new CSV file
merged_df.to_csv('merged_visitors_inflation.csv', index=False)

# Show the first few rows
print(merged_df.head())
