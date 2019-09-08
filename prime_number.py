num = int(input("Input a natural number: ")) # Do not change this line
count = 1
prime = True
while count <= num :
    if num % count == 0 and count != 1 and num != count :
       prime = False
    count = count + 1

if prime:
    print("Prime")
else:
    print("Not prime")