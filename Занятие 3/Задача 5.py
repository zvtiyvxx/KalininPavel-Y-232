# -- coding: utf-8 --
def naim(x,y,z):
    if x < y and x < z:
        return(x)
    elif y < z and y < z:
        return(y)
    elif z < y and z < x:
        return(z)
x = int(input('Введите 1 число '))
z = int(input('Введите 2 число '))
y = int(input('Введите 3 число '))
c = naim(x,y,z)
print(c)




