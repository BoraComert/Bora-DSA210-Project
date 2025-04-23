import pandas as pd

# Load your CSV files
df_tourists = pd.read_csv("milliyetlerine-gore-istanbul-a-gelen-yabanci-turist-sayisi.csv")
df_income = pd.read_csv("daily-median-income.csv")

# Extract year from the 'tarih' column
df_tourists["Year"] = pd.to_datetime(df_tourists["tarih"]).dt.year

# Country name translation dictionary
country_translation = {
    "Rusya": "Russian Federation",
    "Avustralya": "Australia",
    "Çin": "China",
    "Endonezya": "Indonesia",
    "Japonya": "Japan",
    "Kamboçya": "Cambodia",
    "Laos": "Lao People's Democratic Republic",
    "Filipinler": "Philippines",
    "Tayland": "Thailand",
    "Vietnam": "Vietnam",
    "Yeni Zelanda": "New Zealand",
    "Kanada": "Canada",
    "ABD": "United States",
    "Hindistan": "India",
    "Pakistan": "Pakistan",
    "Bangladeş": "Bangladesh",
    "Arnavutluk": "Albania",
    "Ermenistan": "Armenia",
    "Avusturya": "Austria",
    "Azerbaycan": "Azerbaijan",
    "Belçika": "Belgium",
    "Bulgaristan": "Bulgaria",
    "Belarus": "Belarus",
    "İsviçre": "Switzerland",
    "Kıbrıs": "Cyprus",
    "Almanya": "Germany",
    "İspanya": "Spain",
    "Estonya": "Estonia",
    "Finlandiya": "Finland",
    "Fransa": "France",
    "Birleşik Krallık": "United Kingdom",
    "İtalya": "Italy",
    "Kazakistan": "Kazakhstan",
    "Kırgızistan": "Kyrgyz Republic",
    "Hollanda": "Netherlands",
    "Brezilya": "Brazil",
    "Arjantin": "Argentina",
    "Meksika": "Mexico",
    "Suudi Arabistan": "Saudi Arabia",
    "Birleşik Arap Emirlikleri": "United Arab Emirates",
    "Kuveyt": "Kuwait",
    "Katar": "Qatar",
    "Bahreyn": "Bahrain",
    "Umman": "Oman",
    "Irak": "Iraq",
    "Ürdün": "Jordan",
    "Lübnan": "Lebanon",
    "Suriye": "Syria",
    "Mısır": "Egypt",
    "Fas": "Morocco",
    "Cezayir": "Algeria",
    "Tunus": "Tunisia",
    "Libya": "Libya",
    "Yemen": "Yemen",
    "Filistin": "Palestine"
}

# Map Turkish names to English
df_tourists["Entity"] = df_tourists["uyruk"].map(country_translation)

# Drop rows with no mapped country
df_tourists = df_tourists.dropna(subset=["Entity"])

# Merge with income data
df_merged = pd.merge(df_tourists, df_income, on=["Entity", "Year"], how="inner")

# Rename and reorganize columns
df_merged_cleaned = df_merged[[
    "tarih", "uyruk", "Entity", "Code", "ziyaretci_sayisi", "Median income or consumption"
]].rename(columns={
    "Code": "Country Code",
    "Median income or consumption": "Median Income"
})

# Convert 'tarih' to datetime and filter/sort by year
df_merged_cleaned["tarih"] = pd.to_datetime(df_merged_cleaned["tarih"])
df_merged_cleaned = df_merged_cleaned[df_merged_cleaned["tarih"].dt.year.between(2019, 2025)]
df_merged_cleaned = df_merged_cleaned.sort_values(by="tarih")

# Save to CSV
df_merged_cleaned.to_csv("combined_tourist_income_data.csv", index=False)

print("File saved as combined_tourist_income_data.csv")
