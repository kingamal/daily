def main():
    print("\nWelcome to the Real Estate Price Estimator!")

    while True:
        try:
            size_of_property = float(input("Enter the size of the property in square feet: "))
            if size_of_property <= 0:
                print("The size of the property must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the size!")

    while True:
        location = input("Enter the location (city or suburb): ").strip().lower()
        if location == 'city':
            price_per_sqft = 250
            break
        elif location == 'suburb':
            price_per_sqft = 150
            break
        else:
            print("Invalid input. Please write 'city' or 'suburb' only. Try again.")

    estimated_price = size_of_property * price_per_sqft

    print(f"\nThe estimated price for a {size_of_property:.2f} sq ft property in the {location} is: ${estimated_price:.2f}")

if __name__ == "__main__":
    main()