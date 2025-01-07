numbers = [3, 1, 2, 3, 4, 1, 5, 2]

# First solution
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

cleaned_list = remove_duplicates(numbers)
print("List without duplicates:", cleaned_list)

# Second solution - cleaner and more efficient
cleaned_list = list(dict.fromkeys(numbers))
print("List without duplicates:", cleaned_list)