# 2) write a program to findout whether given year is golden jubilee or not from current year and  marriage year 


marriage_year = int(input("Enter marriage year:"))
current_Year = 2026

if current_Year - marriage_year == 50:
    print("It is a Golden Jubilee")
else:
    print("It is not a Golden Jubilee")
print("Have a nice day")