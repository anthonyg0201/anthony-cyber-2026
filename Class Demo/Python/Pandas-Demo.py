# Import the Pandas Library
import pandas as pd

# Read the CSV file
df = pd.read_csv("logs.csv")

# Print the Original DataFrame
print(df)

# Grouping and Summing Data
result = df.groupby("ip")["count"].sum()

# Print Group Results
print("\nGrouped and Summed counts by IP:")
print(result)

# Sorting the results
sorted_result = result.sort_values(ascending=False)

# Print the Sorted Results
print("\nSorted by count descending:")
print(sorted_result)