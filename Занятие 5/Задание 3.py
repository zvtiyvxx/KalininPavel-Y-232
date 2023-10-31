# -- coding: utf-8 --
def stepen(N):
    x = 1
    y = 0
    while x * 2 <= N:
        x *= 2
        y += 1
    return (x,y)
N = int(input('Введите целое число: '))
c = stepen(N)
print(c)
