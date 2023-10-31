# -- coding: utf-8 --
def kvadrati(N):
    i = 1
    while i ** 2 <= N:
        print (i ** 2)
        i += 1
N = int(input('Введите число N: '))
c = kvadrati(N)
print(c)
