# Import pandas
import pandas as pd

df = pd.read_csv("logs.csv")
print(df)
result = df.groupby("ip")["count"].sum()