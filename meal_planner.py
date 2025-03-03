import random

breakfast_options = ["Oatmeal with fruits", "Scrambled eggs and toast", "Smoothie bowl", "Greek yogurt with granola"]
lunch_options = ["Grilled chicken salad", "Quinoa with roasted veggies", "Spaghetti with tomato sauce", "Sushi rolls"]
dinner_options = ["Baked salmon with rice", "Vegetable stir-fry", "Chickpea curry", "Tacos with beans and avocado"]

def suggest_meal(meal_type, options):
    return random.choice(options)

def main():
    breakfast = suggest_meal("breakfast", breakfast_options)
    lunch = suggest_meal("lunch", lunch_options)
    dinner = suggest_meal("dinner", dinner_options)

    print("Welcome to the Meal Planner Assistant!")
    print(f"Breakfast: {breakfast}")
    print(f"Lunch: {lunch}")
    print(f"Dinner: {dinner}")
    print("Enjoy your meals and eat healthy!")

if __name__ == "__main__":
    main()