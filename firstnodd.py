num = int(input("Input an int: ")) 
count = 0
ber = 1

while count < num :
    if ber % 2 == 1 :
        print(ber)
        count = count + 1
        ber = ber + 1
    else :
        ber = ber + 1

