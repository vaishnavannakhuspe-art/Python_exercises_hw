#  1) write a program to convert given days into months and remaining days
days = int(input("Enter no of days:"))

months = days // 30
remaining_days = days % 30

print(f"{days} days = {months} months and {remaining_days} days")