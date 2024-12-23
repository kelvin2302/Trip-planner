import pandas as pd

# Load the data
df = pd.read_csv("restaurants.csv")

# Drop duplicates and null values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

# Splitting multiple cuisine values into separate rows
df = df.assign(Cuisine=df['Cuisine'].str.split(',')).explode('Cuisine')

# Save the normalized data to a new CSV file
df.to_csv("normalized_restaurants.csv", index=False)
