# 1) write a program to findout which person is heaviest person in 4 person. accept 4 person weight from user
person_1 = int(input("Enter 1st person's weight:"))
person_2 = int(input("Enter 2nd person's weight:"))
person_3 = int(input("Enter 3rd person's weight:"))
person_4 = int(input("Enter 4th person's weight:"))

if person_1 > person_2:
    if person_1 > person_3:
        if person_1 > person_4:
            print("person_1 is heaviest")
        else:
            print("person_4 is heaviest")
    else:
        if person_3 > person_4:
            print("person_3 is the heaviest")
        else:
            print("person_4 is the heaviest")
else:
    if person_2 > person_3:
        if person_2 > person_4:
            print("person_2 is the heaviest")
        else:
            print("person_4 is the heaviest")
    else:
        if person_3 > person_4:
            print("person_3 is the heaviest")
        else:    
            print("person_4 is the heaviest")
        
