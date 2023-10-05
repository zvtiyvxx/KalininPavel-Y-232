# -- coding: utf-8 --
# №1
print ('Курс Основы программирования начался')
# №2
print((16823 * 12302) % 3092)
# №3
age = int(input("Введите возраст(цифрой):"))
name = input("Введите имя:")
if name != 'Иван':
    if 0 < age < 75:
        if age >= 16:
            print ('Поздравляем вы поступили в ВГУИТ')
        else:
            print('Сначала нужно окончить школу!')
else:
    print('Иванов не берём')
# №4
seconds = int(input("Введите количество секунд: "))
days = seconds // (24 * 60 * 60)
seconds = seconds - days * (24 * 60 * 60)
hours = seconds // 3600
seconds = seconds - hours * 3600
minutes = seconds // 60
seconds = seconds - minutes * 60
seconds2 = seconds

print(f"{days} дней {hours} часов {minutes} минут {seconds2} секунд")
# №5
n = int(input("Введите число:"))
print(n + n^2 + n^3 + n^4 + n^5)
# №6
x = int(input("Введите значение x:"))
y = int(input("Введите значение y:"))
v = y
y = x
x = v
print ('y:', y)
print ('x:', x)
# №7
number = int(input("Введите число:"))
if number % 2 == 0:
        print('Четное')
else:
        print ('Нечетное')
