import pandas as pd

# Load datasets
city_df = pd.read_csv("./Dataset/City.csv")
list_df = pd.read_csv("./Dataset/list.csv")
food_df = pd.read_csv("./Dataset/indian_food.csv")

# Function to match city with state
def match_city_state(city_name):
    state_name = None
    for idx, row in list_df.iterrows():
        if city_name.lower() in row['Name of City'].lower():
            state_name = row['State']
            break
    return state_name

# Function to suggest famous food based on state
def suggest_food(city_name):
    state_name = match_city_state(city_name)
    if state_name:
        state_food = food_df[food_df['state'] == state_name]
        famous_food = state_food['name'].tolist()
        return famous_food
    else:
        return "State not found for the given city."

# Example usage
city_name = "Mumbai"
suggested_food = suggest_food(city_name)
if suggested_food:
    print(f"Famous food in {city_name}: {', '.join(suggested_food)}")
else:
    print("No famous food found for the given city.")
