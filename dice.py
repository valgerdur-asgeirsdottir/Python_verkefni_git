d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if 1 <= d1 <=6 and  1 <= d2 <=6 :
    d_sum = d1 + d2
    if d_sum == 7 or d_sum == 11 :
        print("Winner")
    elif d_sum == 2 or d_sum == 3 or d_sum == 12 :
        print("Loser")
    else :
        print(d_sum)
else :
    print("Invalid input")
    
