age_int = int(input("Enter your age: "))
if age_int >= 0:
    if age_int > 0 and age_int <= 34:
        print("Young")
    elif age_int > 34 and age_int <= 50:
        print("Mature")
    elif age_int > 50 and age_int <= 69:
        print("Middle-aged")
    else :
        print("Old")
else :
    print("Invalid age")