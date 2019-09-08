
for i in range(10, 100):
    num1 = i // 10
    num2 = i % 10
    sum_num = num1 + num2
    if (sum_num ** 2) == i:
        print(i)

count_div = 0

for i in range(10,100):
    for b in range(1,100):
        if i % b == 0:
            count_div = count_div +1
    if count_div == 10:
        print(i)