# -- coding: utf-8 --
def visocosniu(x):
    if ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0):
        return(print('Да'))
    else:
        return(print('Нет'))
x = int(input('Введите год: '))
c = visocosniu(x)
print(c)
