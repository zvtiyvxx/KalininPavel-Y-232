# -- coding: utf-8 --
def gg(n):
    d = 0
    for i in range(1, n + 1):
        d += i ** 3
    return d
n = int(input('Введите число n '))
c = gg(n)
print(c)
