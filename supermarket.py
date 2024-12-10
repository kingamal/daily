def discount(subtotal):
    if subtotal >= 20 and subtotal <= 50:
        return 0.05
    elif subtotal > 50 and subtotal <= 70:
        return 0.1
    elif subtotal > 70:
        return 0.15
    else:
        return 0

def summary(basket):
    print("\n--- Bill Summary ---")
    subtotal = 0
    for el in basket:
        total_price = el["quantity"] * el["price"]
        print(f"{el["name"]}: {el["quantity"]} x ${el["price"]} = ${total_price:.2f}")
        subtotal += total_price

    tax = subtotal * 0.05
    what_discount = discount(subtotal)
    dicount = subtotal * what_discount if what_discount > 0 else 0
    total = subtotal + tax - dicount
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${dicount:.2f}")
    print(f"Sales Tax (5%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("\nThank you for shopping with us!")

def supermarket():
    print("Welcome to the Supermarket Billing System!")
    num = int(input("Enter the number of items: "))
    basket = []

    if num > 0:
        for i in range(num):
            print(f"\nItem {i+1}:")
            name = input("Name: ")
            price = float(input("Price per unit: "))
            quantity = int(input("Quantity: "))
            item = {"id": i+1, "name": name, "price": price, "quantity": quantity}
            basket.append(item)
        summary(basket)
    else:
        print("There is no item(s) in your basket!")

if __name__ == "__main__":
    supermarket()