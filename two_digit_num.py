count1 = 10
count2 = 99
while count1 <= count2 :
    square = count1 * count1
    if square < 1000 :
        rest = (square % 100)
        if rest == count1 :
            print(count1)   
    count1 += 1