# 3) write a program to findout what kind of fever user has. based upon below criteria 
# input : body temperature as fahrenheit 

# temperature       Fever Type
# --------------------------------  
# 99.1∘F−100.4∘F	  Low-grade	
# 100.6∘F−102.2∘F	  Moderate
# 102.3∘F−105.8∘F	  High-grade	
# >106.0∘F	      Hyperpyrexia

temperature = input("Enter temperatuer in fahrenheit:")
temperature_f = float(temperature)
if temperature_f < 0 or temperature_f > 120:
    print("Invalid temperature")
    exit(1)


if 100.6 > temperature_f >= 99.1:
    print("Person has Low Grade fever")
elif 102.2 >= temperature_f >= 100.6:
    print("Person has Moderate fever")
elif 105.8 >= temperature_f >= 102.3:
    print("Person has High Grade fever")
elif temperature_f >= 106.0:
    print("Person has Hyperpyrexia fever")
else:
    if 99 > temperature_f > 90:
        print("Normal")

