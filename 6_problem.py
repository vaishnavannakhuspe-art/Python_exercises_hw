# 6) write a program to convert given grams into kilograms and remaining grams.


grams = int(input("Enter grams:"))

kilograms = grams//1000
remaining_grams = grams%1000

print(f"{grams}g = {kilograms}kg {remaining_grams}g")


