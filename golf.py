count = 1

while count <= 18 :
    par = int(input(f"Par of hole {count}: ")) 
    score = int(input(f"Score on hole {count}: "))
    if score < (par - 3) :
        print("invalid score")
    elif score == (par - 3) :
        print("albatross")
    elif score == (par - 2):
        print("eagle")
    elif score == (par - 1):
        print("birdie")
    elif score == par :
        print("par")
    elif score == (par + 1) :
        print("bogey")
    elif score == (par +2) :
        print("double bogey")
    elif score == (par + 3) :
        print("triple bogey")
    else :
        print("bad hole")
    count += 1