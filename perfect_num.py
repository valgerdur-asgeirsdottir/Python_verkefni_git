top_num = int(input("Upper number for the range: "))
for i in range(1, top_num+1):
    sum = 0
    for p in range(1,i):
        if i % p == 0:
            sum = sum + p
    if sum == i:
        print(i)
