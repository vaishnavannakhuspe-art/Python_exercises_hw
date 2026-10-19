# 3) 5 10 15 20 25 ..... 500
num = 5 
next = num + 5
print(num, end = " ")
while num < 500 :
    print(next,end=" ")
    num = next
    next = num + 5
print("Done")

