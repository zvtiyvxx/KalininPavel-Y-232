# -- coding: utf-8 --
def shnurki(a, b, l, N):
    return (2 * l + 2 * (N - 1) * a + 2 * (N - 1) * b + a)

a = int(input("Введите расстояние между рядами дырочек (a): "))
b = int(input("Введите расстояние между дырочками в ряду (b): "))
l = int(input("Введите длину свободного конца шнурка (l): "))
N = int(input("Введите количество дырочек в каждом ряду (N): "))

length = shnurki(a, b, l, N)
print(length)
