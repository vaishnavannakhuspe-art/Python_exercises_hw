# 2) 2 4 6 8 10 ...... 200
num = 2 
next = num + 2
print(num, end = " ")
while num < 200 :
    print(next,end=" ")
    num = next
    next = num + 2
print("Done")