import json

def load_recipes(filename):
    with open(filename, 'r') as file:
        recipes = json.load(file)
    return recipes

def find_recipes_by_ingredients(recipes, user_ingredients):
    matching_recipes = []
    for recipe in recipes:
        recipe_ingredients = recipe['ingredients']
        if all(item in user_ingredients for item in recipe_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes

def display_recipes(recipes):
    if recipes:
        print("Here are some recipes you can make:\n")
        for recipe in recipes:
            print(f"Recipe: {recipe['name']}")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}\n")
    else:
        print("No recipes match the ingredients you have.")

def main():
    recipes = load_recipes('recipes.json')

    ingredients = input("Enter a list of ingredients, separated by commas: ")
    list_of_ingredients = [item.strip().lower() for item in ingredients.split(',')]

    matching_recipes = find_recipes_by_ingredients(recipes, list_of_ingredients)
    display_recipes(matching_recipes)

if __name__ == "__main__":
    main()
