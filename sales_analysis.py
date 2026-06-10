import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales.csv")

print(df.head())
print(df.describe())

plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
