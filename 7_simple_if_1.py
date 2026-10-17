#  1) write a program to accept english month number from user. then display name of festival come in given month.

month_no = int(input("Enter month no:"))
indian_festivals = {
    1: "Makar Sankranti / Pongal",2: "Maha Shivaratri",3: "Holi",4: "Baisakhi / Gudi Padwa",5: "Buddha Purnima",6: "Hemis Festival",7: "Jagannath Rath Yatra",8: "Raksha Bandhan",9: "Ganesh Chaturthi",10: "Durga Puja / Navaratri",11: "Diwali",12: "Christmas"
}
festival = ""
Month = indian_festivals.keys()

if month_no in Month:
    festival = indian_festivals.get(month_no)
    print(festival)