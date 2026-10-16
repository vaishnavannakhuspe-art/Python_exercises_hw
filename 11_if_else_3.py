# 3) write a program to findout which shape is lesser in two different farm from given length and width of two farm

length_1 = int(input("Enter the 1st length:"))
width_1 = int(input("Enter the 1st width:"))
length_2 = int(input("Enter the 2nd length:"))
width_2 = int(input("Enter the 2nd width:"))

area_1 = length_1 * width_1
area_2 = length_2 * width_2

if area_1 == area_2:
    print("Both shapes have same size")
    exit(1)

if area_1 > area_2:
    print("Shape1 is greater than Shape2")
else:
    print("Shape2 is greater than Shape1")