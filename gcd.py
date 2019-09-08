m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

for i in range(1,m+1):
    if m % i == 0 and n % i == 0:
        gcd = i
        
print (gcd)

