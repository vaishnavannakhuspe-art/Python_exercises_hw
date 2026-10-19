# 1) 50 49 48 ...... 1
num = 50
next = num - 1
print(num,end = " ")
while num>1:
    print(next,end= " ")
    num = next
    next = num - 1
print("Done")