import pandas as pd

# Load your datasets
df_weather = pd.read_csv("weather_visitor_merged_file.csv")  
df_income = pd.read_csv("Country_Income_Classification.csv") 


#Incase there are whitelines we clear them
df_income.columns = df_income.columns.str.strip()

# Keep only necessary columns and drop duplicates by country 3 letter  code
df_income_cleaned = df_income[['Code', 'Income classification']].drop_duplicates(subset='Code')

# Add the Income classification to the weather and tourist set
merged_df = df_weather.merge(df_income_cleaned, left_on='Country', right_on='Code', how='left')

# Drop the redundant 'Code' column
merged_df.drop(columns='Code', inplace=True)

# Save or inspect result
merged_df.to_csv("merged_output.csv", index=False)

