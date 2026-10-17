#  write a program to accept 3 color value from user for red, green & blue if the range of each and every color is in between 0 to 255. display message it is valid color otherwise display message it is not valid color 

red = int(input("Enter colour value:"))
blue = int(input("Enter colour value:"))
green = int(input("Enter colour value:"))

if 0 < red < 255:
    if 0 < blue < 255:
        if 0 < green <255:
            print("Valid colour")
        else:
            print("Colour Invalid")
    else:
        print("Colour Invalid")
else:
    print("Colour Invalid")