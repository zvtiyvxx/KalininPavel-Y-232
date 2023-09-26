a = int(input('Введите число a '))
b = int(input('Введите число b '))
while a != b:
    print(a)
    if a < b:
        a += 1
    elif b < a:
        a -= 1
print(b)
