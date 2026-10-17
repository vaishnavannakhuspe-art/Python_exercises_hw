# 1) write a program to findout whether given year is sliver jubilee or not from current year and  marriage year 

marriage_year = int(input("Enter marriage year:"))
current_Year = 2026

if current_Year - marriage_year == 25:
    print("It is a Silver Jubilee")
else:
    print("It is not a Silver Jubilee")
print("Have a nice day")