first_int = int(input("First: "))
step_int = int(input("Step: "))

print(first_int, end=" ")
num = first_int
sum_series = num
while sum_series < 100:
    num = num + step_int
    print(num, end=" ")
    sum_series = sum_series + num

print(" ")
print("Sum of series:", sum_series)
