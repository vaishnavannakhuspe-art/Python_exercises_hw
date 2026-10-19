# 4) 1 2 4 7 11 16 ..... 100
num = 1
next = 1
print(num,end=" ")
final = num + next
print(final,end=" ")
num = num+1
next= final
final = num + next
print(final,end=" ")
num = num+1
next = final
final = num + next
print(final,end=" ")
while final < 100:
    num = num+1
    next = final 
    final = num + next
    print(final,end=" ")
print("Done")

