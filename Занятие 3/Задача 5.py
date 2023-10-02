# -- coding: utf-8 --
x = int(input('Введите 1 число '))
z = int(input('Введите 2 число '))
y = int(input('Введите 3 число '))
def naim():
    if x < y and x < z:
        print(x)
    elif y < z and y < z:
        print(y)
    elif z < y and z < x:
        print(z)
        return
naim()




