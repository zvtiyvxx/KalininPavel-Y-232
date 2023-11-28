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

matrix = []
with open('Kalinin_Pavel_У232_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split())) 
        matrix.append(row)
    print("Прочитанная матрица:")
    for row in matrix:
        print(row)

with open('Kalinin_Pavel_У232_vivod.txt', 'w') as file:
    max_element, row_index, col_index = max_abs_element(matrix)
    print(f"Наибольший по модулю элемент: {max_element}", file=file)

    new_matrix = [row[:col_index] + row[col_index + 1:] for i, row in enumerate(matrix) if i != row_index]
    new_matrix = [row[:] for row in new_matrix if row != matrix[row_index]]
    for row in new_matrix:
        print(f"Новая матрица:{row}", file=file)

