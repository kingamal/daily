GROCERY_LIST = ["apples", "bread", "milk", "eggs", "bananas"]

def groceries(grocery_list):
    grocery_list.append("beans")
    grocery_list.remove("bread")
    grocery_list.sort()
    print("Updated Grocery List:")
    print(*grocery_list, sep="\n")

if __name__ == '__main__':
    groceries(GROCERY_LIST)