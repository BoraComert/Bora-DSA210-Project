import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

#Load data
df = pd.read_csv("/Users/boracomert/Desktop/Bora-DSA210-Project-1/merged_output.csv")

# Prepare Season Jnauary,February,March = winter ; April , May, June = spring ; July, August, Septembre = Summer; October, November ,december = winter 
df['Date'] = pd.to_datetime(df['Date'])
month_to_season = {1: 'Winter', 4: 'Spring', 7: 'Summer', 10: 'Autumn'}
df['Season'] = df['Date'].dt.month.map(month_to_season)

# 3. Group by Season and Income Classification
income_group = df.groupby(['Season', 'Income classification'])['ziyaretci_sayisi'].sum().reset_index()
income_pivot = income_group.pivot(index='Season', columns='Income classification', values='ziyaretci_sayisi').fillna(0)

# 4. Drop columns (income groups) with all zeros
income_pivot = income_pivot.loc[:, (income_pivot != 0).any(axis=0)]

# 5. Drop rows (seasons) with all zeros (optional but safe)
income_pivot = income_pivot[(income_pivot.T != 0).any()]

# 6. Chi-Square Test
chi2_income, p_income, dof_income, _ = chi2_contingency(income_pivot)

print("Chi-Square Test: Istanbul Season vs. Country Income Classification")
print(f"Chi2 statistic: {chi2_income:.3f}")
print(f"P-value: {p_income:.5f}")
print(f"Degrees of freedom: {dof_income}")

# 7. Plot the pivot table
income_pivot.plot(kind='bar', figsize=(12, 7), width=0.7)
plt.title('Tourist Numbers by Istanbul Season and Country Income Group')
plt.ylabel('Total Tourists')
plt.xlabel('Season (Istanbul)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
