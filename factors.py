num = int(input("Input an int: "))
count = 1

while count <= num :
    if num % count == 0 :
        print(count)
    count = count + 1