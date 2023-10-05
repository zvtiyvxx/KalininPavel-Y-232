# -- coding: utf-8 --
def gg(n):
    for i in range(n,0,-1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
n = int(input("Введите число n (n <= 9): "))
gg(n)
