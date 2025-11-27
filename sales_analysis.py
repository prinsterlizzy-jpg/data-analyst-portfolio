import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
monthly = df.groupby('Month')['Total Revenue'].sum()
monthly.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("monthly_sales_trend.png")
