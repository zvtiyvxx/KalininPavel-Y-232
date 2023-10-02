# -- coding: utf-8 --
n = int(input('Введите число n '))
b = 0
c = 1
for i in range(1, n + 1):
    c *= i
    b += c
print(b)
