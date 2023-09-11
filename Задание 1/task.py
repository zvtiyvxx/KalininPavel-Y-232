# №1
print ('Курс Основы программирования начался')
# №2
print((16823 * 12302) % 3092)
# №3
age = int(input("Введите возраст(цифрой):"))
name = input("Введите имя:")
if 0 < age < 75:
    if age >= 16:
        print ('Поздравляем вы поступили в ВГУИТ')
    elif age < 16:
        print('Сначала нужно окончить школу!')
# №4
second = int(input("Введите количество секунд:"))
print('Минуты:', second // 60, 'Часы:', second // 3600, 'Дни:', second // (3600*24))
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
