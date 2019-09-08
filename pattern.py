stars_int = int(input("Number of stars: "))
ninja = "*"
if stars_int > 0:
    print(ninja)
    for i in range(1, stars_int):
        ninja = ninja + "*"
        print(ninja)
