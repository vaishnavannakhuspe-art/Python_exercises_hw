# 2) write a program to convert hexadecimal number into binary number
# input("Enter number: ")
num = "B2E"
hxd_dict = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
decimal_no = 0
power_of_16 = len(num)-1
for i in num:
    if i in hxd_dict:
        elem = hxd_dict.get(i)
    else:
        elem = int(i)
    decimal_no += elem * (16**power_of_16)
    power_of_16 -= 1
hxd_to_dec = decimal_no
print(hxd_to_dec)

def dec_to_binary(hxd_to_dec):
    if hxd_to_dec>0:
        reminder = hxd_to_dec % 2 
        hxd_to_dec = hxd_to_dec // 2 
        dec_to_binary(hxd_to_dec)
        print(reminder,end=' ')
dec_to_binary(hxd_to_dec)

    

