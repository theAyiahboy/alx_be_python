# Get user input for weather condition
weather_input = input("What's the weather like today? (sunny/rainy/cold): ")

# Dictionary to store weather recommendations
weather_recommendations = {
    "sunny": "Wear a t-shirt and sunglasses.",
    "rainy": "Don't forget your umbrella and a raincoat.",
    "cold": "Make sure to wear a warm coat and a scarf."
}

# Check if the weather condition is in our recommendations
if weather_input in weather_recommendations:
    print(weather_recommendations[weather_input])
else:
    print("Sorry, I don't have recommendations for this weather.")
