# 1 0 1 0 1
# 1 0 1 0
# 1 0 1
# 1 0
# 1
for row in range(5,0,-1):
    print("")
    for column in range(0,row):
        if column % 2 == 0:
            print("1",end = " ")
        else:
            print("0",end = " ")