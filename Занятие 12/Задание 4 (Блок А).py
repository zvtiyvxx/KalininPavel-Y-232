def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

number = int(input("Введите натуральное число: "))
result = sum_of_digits(number)
print("Сумма цифр числа", number, "равна", result)

