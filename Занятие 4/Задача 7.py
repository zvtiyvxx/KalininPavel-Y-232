# -- coding: utf-8 --
def gg(n):
    b = 0
    d = 1
    for i in range(1, n + 1):
        d *= i
        b += d
    return d
n = int(input('Введите число n '))
c = gg(n)
print(c)
