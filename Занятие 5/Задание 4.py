# -- coding: utf-8 --
def sport(x,y):
    x *= 1000
    y *= 1000
    i = 0
    d = 0
    while x <= y:
        d = x * 0.1
        x += d
        i += 1
    return(i)
x = int(input('Введите количество киллометров в первый день: '))
y = int(input('Введите количество киллометров, которые спортсмен должен пробежать: '))
c = sport(x,y)
print(c)
