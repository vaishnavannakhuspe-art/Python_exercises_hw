# 4) write a program to findout obesity level of person in india from given height and weight. 

# accept weight and height (foot & inch)
# calculate BMI (Body to mass index)
# display Obesity level 

# Category	        BMI (lbs/(in)2)	        
# -----------------------------------------------------
# Underweight	        <18.5	           
# Normal	            18.5−22.9	        
# Overweight	        23.0−24.9	        
# Obesity Class I	    25.0−29.9	        
# Obesity Class II	≥30.0	         


weight = int(input("Enter weight in Kg:"))
height = float(input("Enter height [foot.inch] format:"))

weight_lbs = weight * 2.20
foot_to_inches= (height//1)*12
inches = (height%1)*10
height_inches = foot_to_inches + inches

bmi = (weight_lbs*703)/(height_inches*height_inches)

if bmi >= 30:
    print("Obesity level II")
elif bmi >= 25:
    print("Obesity level I")
elif bmi >= 23:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")





