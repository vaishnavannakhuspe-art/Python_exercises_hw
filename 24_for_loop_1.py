# write a program to convert all negative values in list as positive value in other list. keep positive values in list as it is 
list_1 = [-1,2,-3,4,-5,-6,7,-8,9,10]
list_2 = []
for num in list_1:
    if num < 0:
        num = 0 -(-num)
        list_2.append(num)
    else:
        list_2.append(num)
print(list_2)