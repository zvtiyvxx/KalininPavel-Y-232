# -- coding: utf-8 --
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
def sovpad(a,b,c):
    if a == b == c:
        print('3')
    elif a == b or b == c or a == c:
        print('2')
    else:
        print('3')
        return
c = sovpad(a,b,c)
print(c)
