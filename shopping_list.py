shopping_list = ["apples", "bananas", "oranges", "milk", "bananas", "bread", "apples"]

def print_shopping_list(items):
    unique_items = sorted(set(items))
    print("Organized Shopping List:")
    for item in unique_items:
        print(f"- {item}")

if __name__ == "__main__":
    print_shopping_list(shopping_list)