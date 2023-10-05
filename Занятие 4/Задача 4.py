# -- coding: utf-8 --
def gg(n):
    d = 0
    for i in range(n):
        b = int(input('Введите каждое из чисел: '))
        d += b
    return d
n = int(input("Введите количество чисел: "))
c = gg(n)
print(c)
