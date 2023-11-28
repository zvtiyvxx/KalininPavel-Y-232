# -- coding: utf-8 --
def max_abs_element(matrix):
    max_element = 0
    max_i = 0
    max_j = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current_abs = abs(matrix[i][j])  
            if max_element is None or current_abs > abs(max_element):
                max_element = matrix[i][j]  
                max_i = i  
                max_j = j  
    
    return max_element, max_i, max_j

n = int(input("Введите размер квадратной матрицы: "))

matrix = []
for i in range(n):
    row = list(map(int, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
    matrix.append(row)
print("Введенная матрица:")
for row in matrix:
    print(row)

max_element, row_index, col_index = max_abs_element(matrix)
print(f"Наибольший по модулю элемент: {max_element}")

new_matrix = [row[:col_index] + row[col_index + 1:] for i, row in enumerate(matrix) if i != row_index]
new_matrix = [row[:] for row in new_matrix if row != matrix[row_index]]

print("Новая матрица:")
for row in new_matrix:
    print(row)

