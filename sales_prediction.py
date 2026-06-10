import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("retail_sales.csv")

X = df[['Month']]
y = df['Sales']

model = LinearRegression()
model.fit(X,y)

future_months = [[13],[14],[15],[16]]

predictions = model.predict(future_months)

for month,pred in zip(range(13,17),predictions):
    print(f"Month {month}: {pred:.2f}")
