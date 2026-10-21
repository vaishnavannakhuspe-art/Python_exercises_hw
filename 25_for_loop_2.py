# write a program to count no of vowels and consonant in given string using for loop
string = "the easylearn acadmy, bhavnagar"
vowels = 0
consonants = 0
for i in string:
    if i in "aeiou":
        vowels += 1
    else:
        consonants += 1
print("Number of vowels:",vowels)
print("Number of consonants:",consonants)