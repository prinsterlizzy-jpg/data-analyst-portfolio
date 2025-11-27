import pandas as pd

df = pd.read_csv("customers.csv")
summary = df.groupby('Age Group')['Total Spending'].sum()
print(summary)
