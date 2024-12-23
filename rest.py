import pandas as pd

# Load the data
df = pd.read_csv("normalized_restaurants.csv")

# Function to recommend the best restaurants for a particular cuisine in a specific city
def recommend_restaurants(city, cuisine):
    city_cuisine_df = df[(df['City'] == city) & (df['Cuisine'] == cuisine)]
    sorted_city_cuisine_df = city_cuisine_df.sort_values(by='Rating', ascending=False)
    return sorted_city_cuisine_df[['Name', 'Location', 'Rating', 'Cost']].head()

# Input city and cuisine
city_input = 'Delhi'
cuisine_input = 'North Indian'

# Get recommendations
recommendations = recommend_restaurants(city_input, cuisine_input)
print(recommendations)
