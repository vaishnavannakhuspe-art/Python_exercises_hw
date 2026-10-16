# 5) write a program to convert given inches into foot and remaining inches

inches = int(input("Enter inches:"))

foot = inches//12
remaining_inches = inches%12

print(f"{inches} inches = {foot} foot and {remaining_inches} inches")