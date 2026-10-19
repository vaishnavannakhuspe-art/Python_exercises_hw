# 1 4 9 16 25 36  ..... 1000
num = 1
square = num*num
print (square,end=" ")
num = num + 1
square = num*num
print (square,end=" ")
num = num + 1
square = num*num
print (square,end=" ")
while square < 1000:
    num = num + 1
    square = num*num
    print (square,end=" ")
print("Done")

