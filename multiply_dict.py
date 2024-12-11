def multiply():
    grocery_list = {
        "apples": 5,
        "bananas": 2,
        "milk": 1,
        "bread": 1
    }
    for k, v in grocery_list.items():
        grocery_list[k] = v * 10

    print(grocery_list)

if __name__ == "__main__":
    multiply()