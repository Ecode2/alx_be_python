def get_weather_advice(weather):
    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()
    advice = get_weather_advice(weather)
    print(advice)

if __name__ == "__main__":
    main()