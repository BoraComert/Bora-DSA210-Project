import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load the data
file_path = 'merged_visitors_inflation.csv'  # update the path if needed
df = pd.read_csv(file_path)

# Check the first few rows (optional)
print(df.head())

# --- Visitor Numbers vs Inflation ---

# Calculate Pearson correlation
visitor_inflation_corr, _ = pearsonr(df['ziyaretci_sayisi'], df['YoY_Inflation (%)'])

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['ziyaretci_sayisi'], df['YoY_Inflation (%)'])
plt.title(f'Visitor Numbers vs Inflation\nPearson Correlation: {visitor_inflation_corr:.2f}')
plt.xlabel('Visitor Numbers')
plt.ylabel('YoY Inflation (%)')
plt.grid(True)
plt.show()

print(f"Visitor vs Inflation Pearson Correlation: {visitor_inflation_corr:.2f}")

# --- Visitor Numbers vs Exchange Rate ---

# Calculate Pearson correlation
visitor_exchange_corr, _ = pearsonr(df['ziyaretci_sayisi'], df['tr/usd_exchange_rate'])

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['ziyaretci_sayisi'], df['tr/usd_exchange_rate'])
plt.title(f'Visitor Numbers vs TR/USD Exchange Rate\nPearson Correlation: {visitor_exchange_corr:.2f}')
plt.xlabel('Visitor Numbers')
plt.ylabel('TR/USD Exchange Rate')
plt.grid(True)
plt.show()

print(f"Visitor vs Exchange Rate Pearson Correlation: {visitor_exchange_corr:.2f}")
