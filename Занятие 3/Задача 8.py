# -- coding: utf-8 --
def sovpad(a,b,c):
    if a == b == c:
        return(3)
    elif a == b or b == c or a == c:
        return(2)
    else:
        return(3)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
c = sovpad(a,b,c)
print(c)
