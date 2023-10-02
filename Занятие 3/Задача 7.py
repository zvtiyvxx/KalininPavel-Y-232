# -- coding: utf-8 --
x = int(input('Введите год: '))
def visocosniu(x):
    if ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0):
        print('Да')
    else:
        print('Нет')
        return
c = visocosniu(x)
print(c)
