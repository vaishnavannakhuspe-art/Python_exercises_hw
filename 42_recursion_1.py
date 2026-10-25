# 1) write a program to convert octal number into binary number
def octal_to_binary(num):
    if num>0:
        reminder = num % 2 
        num = num // 2 
        octal_to_binary(num)
        print(reminder,end=' ')
num = int(input("Enter a number:"))
octal_to_binary(num)