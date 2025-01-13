numbers = (10, 5, 8, 20, 15)

unique_numbers = set(numbers)
sorted_numbers = sorted(unique_numbers, reverse=True)

if len(sorted_numbers) > 1:
    second_largest = sorted_numbers[1]
    print("The second largest number is:", second_largest)
else:
    print("There is no second largest number.")
