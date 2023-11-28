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

matrix = []
with open('Kalinin_Pavel_У232_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split())) 
        matrix.append(row)
    print("Прочитанная матрица:")
    for row in matrix:
        print(row)

k = int(input('Введите число k:'))

count, max_element = max_cratnoe(matrix, k)

with open('Kalinin_Pavel_У232_vivod.txt', 'w') as file:
    print(f"Количество элементов, кратных {k}: {count}", file=file)
    print(f"Наибольший элемент, кратный {k}: {max_element}", file=file)