# 1) create function that will display addition, subtraction, multiplication, division of given 2 number.
def action_on_num(num1,num2):
    addition = num1+num2
    subtraction = num1-num2
    multiplication = num1*num2
    division = num1/num2
    return addition,subtraction,multiplication,division
result = action_on_num(5,5)
print(result)

