def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_temperature_input():
    while True:
        try:
            return float(input("Enter the temperature value: "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_conversion_choice():
    while True:
        try:
            print("Temperature Converter")
            print("Choose the conversion:")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def convert_temperature(choice, temperature):
    if choice == 1:
        return celsius_to_fahrenheit(temperature), "F"
    elif choice == 2:
        return fahrenheit_to_celsius(temperature), "°C"
    elif choice == 3:
        return celsius_to_kelvin(temperature), "K"
    elif choice == 4:
        return kelvin_to_celsius(temperature), "°C"

def main():
    temperature = get_temperature_input()
    choice = get_conversion_choice()
    converted_temperature, unit = convert_temperature(choice, temperature)
    print(f"Converted temperature: {converted_temperature} {unit}")

if __name__ == "__main__":
    main()