Sales Performance Analysis (Excel + Python)

📊 Sales Performance Analysis — 12-Month Sales Dataset

Overview

This project analyzes 12 months of sales data using Excel and Python (Pandas, Matplotlib) to uncover revenue trends, top-performing products, and seasonal patterns.

⸻

🔧 Tools Used
	•	Excel (PivotTables, Charts, Data Cleaning)
	•	Python (Pandas, Matplotlib)
	•	CSV Dataset

⸻

📁 Project Files
	•	sales_data.csv
	•	sales_analysis.py
	•	sales_template.xlsx
	•	monthly_sales_trend.png
	•	Report PDF 

⸻

🛠 Key Tasks Performed

Excel
	•	Cleaned raw dataset (duplicates, missing values)
	•	Created PivotTables:
	•	Revenue by Month
	•	Revenue by Product
	•	Top 10 Products
	•	Designed charts (bar, line, pie)
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
plt.show()

📈 Insights
	•	Product A generated 35% of total revenue.
	•	Peak sales in June, September, and December.
	•	Electronics category contributed 52% of total revenue.

⸻

✅ Conclusion

The analysis highlights clear seasonal patterns and identifies high-performing products, supporting better inventory and marketing decisions.

