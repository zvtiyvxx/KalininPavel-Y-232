# -- coding: utf-8 --
def gg(a,b):
    while a > b:
    if a % 2 != 0:
        return(a)
    a -= 1
if b % 2 != 0:
        return(b)
a = int(input('Введите a '))
b = int(input('Введите b, должно быть меньше a '))
c = gg(a,b)
print(c)
