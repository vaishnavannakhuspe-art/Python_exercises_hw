#findout minimum and maximum number from unsorted list without using loop
unsorted_list = [42, 11, 88, 3, 65, 19, 74, 31, 5, 92, 53, 27, 81, 14, 59]
list1 = sorted(unsorted_list)
list2 = sorted(unsorted_list,reverse = True)
max_num = list(list2)[0]
min_num = list(list1)[0]

print(f"maximum number in the unsorted_list is {max_num}")
print(f"minumum number in the unsorted_list is {min_num}")