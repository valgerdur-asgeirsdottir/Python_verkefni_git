num = int(input("Enter an integer: "))
total = 0
even = 0
odd= 0
biggest = 0

if num > 0 :
    while num > 0 :
        if num > biggest:
            biggest = num #
        total = total + num
        print("Cumulative total: ", total)
        if num % 2 == 0 :
            even += 1
        else :
            odd += 1
        num = int(input("Enter an integer: "))
    else :
        print("Largest number:", biggest)
        print("Count of even numbers:", even)
        print("Count of odd numbers:", odd)


    

