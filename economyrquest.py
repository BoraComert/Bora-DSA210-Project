import pandas as pd

df = pd.read_csv("milliyetlerine-gore-istanbul-a-gelen-yabanci-turist-sayisi.csv")

print(df.groupby("uyruk")["ziyaretci_sayisi"].sum(numeric_only=True).sort_values(ascending=False))