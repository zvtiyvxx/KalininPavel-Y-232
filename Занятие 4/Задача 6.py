# -- coding: utf-8 --
def gg(n):
    d = 1
    for i in range(1, n + 1):
        d *= i
    return d
n = int(input('Введите число n '))
c = gg(n)
print (c)

