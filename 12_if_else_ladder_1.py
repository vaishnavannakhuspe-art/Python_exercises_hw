#  1) write a program to accept 5 subject marks from user. 
#    make total of it  
#    find percentage using total 
#    and display grade as per below rules 
#   ------------------------------------
#    percentage      Grade 
#   >90             Excellent 
#   >80             A+ 
#   >70             A 
#   >60             B 
#   >50             C 
#   >40             Pass 
#   otherwise       Poor 
total_marks = 500 

subject_1_marks = int(input("Enter 1st subject marks:"))
subject_2_marks = int(input("Enter 2nd subject marks:"))
subject_3_marks = int(input("Enter 3rd subject marks:"))
subject_4_marks = int(input("Enter 4th subject marks:"))
subject_5_marks = int(input("Enter 5th subject marks:"))

total_subject_marks = subject_1_marks + subject_2_marks + subject_3_marks + \
                    subject_4_marks + subject_5_marks

percentage = (total_subject_marks/total_marks)*100

if percentage >= 90:
    print("Student has Excellent Grade")
elif 90 > percentage >= 80:
    print("Student has A+ Grade")
elif 80 > percentage >= 70:
    print("Student has A Grade")
elif 70 > percentage >= 60:
    print("Student has B Grade")
elif 60 > percentage >= 50:
    print("Student ha C Grade")
elif 50 > percentage >= 40:
    print("student is Pass")
else:
    print("Student is poor in studies")

print(total_subject_marks)
print(percentage)