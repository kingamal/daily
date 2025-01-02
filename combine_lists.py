def combine_lists():
    list1 = [5, 3, 8, 6, 3]
    list2 = [7, 2, 5, 9, 8]
    list3 = list1 + list2
    list3 = list(dict.fromkeys(list3))
    list3.sort()
    print(list3)

if __name__ == "__main__":
    combine_lists()