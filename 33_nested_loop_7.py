    #       1
    #      2  1
    #     2  1  2
    #    1  2  1  2
    #   1  2  1  2  1
for row in range(5,0,-1):
    print("") 
    for index in range(0,6-row):
        if index%2==0:
            print("1",end=" ")
        else:
            print("2",end=" ")
        
        