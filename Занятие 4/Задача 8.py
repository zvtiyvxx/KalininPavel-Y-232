# -- coding: utf-8 --
n = int(input("Введите число n (n <= 9): "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
