# 6) create function that convert fahrenheit into celsius from given fahrenheit. 
# C = (°F - 32) × 5/9
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*(5/9)
    approx_celsius = round(celsius,2)
    return approx_celsius
result = convert_to_celsius(99)
print(result)
