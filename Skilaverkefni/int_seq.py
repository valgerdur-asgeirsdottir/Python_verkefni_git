num = int(input("Enter an integer: "))
total = 0
even = 0
odd= 0
biggest = 0

if num > 0 : #nothing happens if the first number is not bigger than zero
    while num > 0 :
        if num > biggest: #if this num is bigger than the current biggest num
            biggest = num #assign biggest to this num
        total = total + num
        print("Cumulative total: ", total) #print the total each time the loop runs
        if num % 2 == 0 :
            even += 1 #count every even number
        else :
            odd += 1 #count every odd number
        num = int(input("Enter an integer: "))
    else :
        print("Largest number:", biggest)
        print("Count of even numbers:", even)
        print("Count of odd numbers:", odd)


    

