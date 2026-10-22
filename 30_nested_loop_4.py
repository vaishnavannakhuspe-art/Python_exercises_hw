# 1
# 2 3
# 4 5 6 
# 7 8 9 10
num = 0
for row in range(1,5):
    print("")
    for colum in range(0,row):
        num += 1
        print(num,end=" ")