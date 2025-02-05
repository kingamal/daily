temperatures_fahrenheit = [32, 50, 77, 100, 212]
temperatures_celsius = [(x-32)*5/9 for x in temperatures_fahrenheit]
print(f'Temperatures is Fahrenheit: {temperatures_fahrenheit}')
print(f'Temperatures is Celsius: {temperatures_celsius}')