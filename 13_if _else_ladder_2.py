# 2) write a program to display Greeting message based upon time given by user 
    # 6.00 to 11.59
    # show message Good Morning

    # Good Afternoon
    # 12 to  17
    # show message : Good Afternoon 

    # 17.01 – 22.00 
    # show message : Good Evening

    # otherwise 
    # show message :  good night 
time_1 = (input("Enter the time:"))
time = float(time_1)
if time > 24 or time < 0:
    print("Invalid time")
    exit(1)

if time >= 6 and time < 12:
    print("Good Morning")
elif time >=12 and time < 17:
    print("Good Afternoon")
elif time >= 17 and time < 22:
    print("Good Evening")
else:
    print("Good Night")
