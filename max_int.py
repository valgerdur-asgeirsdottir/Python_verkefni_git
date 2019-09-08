#1. let the user input an integer
#2. if the first input is < 0 do nothing
#3. let the user continue inputing integers until int < 0
#4. when the input is > 0 print the biggest typed integer
num_int = int(input("Input a number: "))
max_int = num_int
if num_int > 0:
    while num_int > 0 :
        if num_int > max_int:
            max_int = num_int
        num_int = int(input("Input a number: "))

    print("The maximum is", max_int)