weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line

weight_float = float(weight_str)
height_m_float = float(height_str)/100

bmi = weight_float / height_m_float**2

print("BMI is: ", bmi) # do not change this line
