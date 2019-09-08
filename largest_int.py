num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

if num1 > (num2 and num3):
    max_int = num1
elif num2 > (num1 and num3):
    max_int = num2
else :
    max_int = num3

print("The maximum is: ", max_int) # Do not change this line
