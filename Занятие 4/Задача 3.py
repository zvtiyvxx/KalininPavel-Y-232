a = int(input('Введите a '))
b = int(input('Введите b, должно быть меньше a '))
while a > b:
    if a % 2 != 0:
        print(a)
    a -= 1
if b % 2 != 0:
        print(b)