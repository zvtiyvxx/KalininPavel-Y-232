# -- coding: utf-8 --
def gg(n):
    a = 0
    b = 1
    s = 0
    for i in range(n):
        s += a
        a, b = b, a + b 
    return s
n = int(input("Введите количество чисел Фибоначчи: "))
c = gg(n)
print(c)
