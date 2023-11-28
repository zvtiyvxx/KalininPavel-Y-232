# -- coding: utf-8 --
def max_cratnoe(matrix, k):
    count = 0 
    max_element = 0
    
    for row in matrix:
        for element in row:
            if element % k == 0:
                count += 1
                if element > max_element:
                    max_element = element
    
    return count, max_element

n = int(input("Введите размер квадратной матрицы: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Введите элемент [{i}][{j}]: "))  # запрашиваем у пользователя элементы матрицы
        row.append(element)
    matrix.append(row)

k = int(input("Введите число k: "))

count, max_element = max_cratnoe(matrix, k)

print(f"Количество элементов, кратных {k}: {count}")
print(f"Наибольший элемент, кратный {k}: {max_element}")
