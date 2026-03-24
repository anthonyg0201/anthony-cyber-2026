# import libraries
import requests
import pandas as pd

# Send a Get Request
response = requests.get("https://jsonplaceholder.typicode.com/comments")

# Convert response to JSON
data = response.json()

# Create a Dataframe
df = pd.DataFrame(data)

# Display the First 5 Rows
print(df.head())