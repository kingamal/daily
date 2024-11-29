weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}

def run_weather():
    print(f"/nWhat's the weather like today?")
    print("1. Sunny ☀️")
    print("2. Rainy 🌧")
    print("3. Cloudy ⛅️")
    print("4. Snowy ❄️")
    choice = int(input("Choose 1, 2, 3 or 4: "))
    
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        print(weather_activities[str(choice)])
        print("Stay safe and enjoy the weather! 🌈")
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    run_weather()
