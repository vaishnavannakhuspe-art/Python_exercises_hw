    #       1
    #      2  1
    #     2  1  2
    #    1  2  1  2
    #   1  2  1  2  1
num = 1
for row in range(5,0,-1):
    print("") 
    space = 1
    while space<row:
        print("",end=" ")
        space += 1
    for index in range(0,6-row):
        if num == 1:
            print("1",end=" ")
            num = 2
        else:
            print("2",end=" ")
            num = 1
        
        