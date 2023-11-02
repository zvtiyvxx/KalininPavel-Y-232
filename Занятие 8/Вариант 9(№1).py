# -- coding: utf-8 --
def sum_of_digits(n):
    return sum(int(digit)for digit in str(n))
def find_steps_to_zero(number):
    steps = 0
    while number > 0:
        number -= sum_of_digits(number)
        steps += 1
    return steps
n = int(input("Введите заданное число: "))
steps_to_zero = find_steps_to_zero(n)
print(steps_to_zero)
