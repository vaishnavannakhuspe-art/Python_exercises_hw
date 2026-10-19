# 6) 1 8 27 64 ...... 10000
num = 1
num = num + 1
cube = num**3
print (cube,end=" ")
num = num + 1
cube = num**3
print (cube,end=" ")
while cube < 10000:
    num = num + 1
    cube = num**3
    print (cube,end=" ")
print("Done")



