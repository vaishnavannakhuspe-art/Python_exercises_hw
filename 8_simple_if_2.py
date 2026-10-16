# 2) write a program to accept week day number from user. then display name of day. 
# // input : 1 output : monday 
# // input : 2 output : tuesday 
# // input : 3 output : wednesday

day = int(input("Enter day no:"))

week = { 1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",
        6:"saturday",7:"sunday"}

day_no = week.keys()

if day in day_no:
    Day = week.get(day)
    print(Day)