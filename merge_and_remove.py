list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

def merge_and_remove(list1, list2):
    merged_list = list1 + list2
    result_list = [item for item in merged_list if item not in list1 or item not in list2]
    return result_list

updated_list = merge_and_remove(list1, list2)

print("Updated list after removing common items:", updated_list)