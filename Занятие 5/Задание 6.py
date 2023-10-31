# -- coding: utf-8 --
def setchiksrznach():
    count = 0
    x = 1
    j = 1
    sum = 0
    while x != 0:
      x = int(input('Введите целое неотрицательное число (0 для завершения): '))
      if x == 0:
        break  
      else:
        sum += x 
        count += 1
    j = sum / count
    return(j)
c = setchiksrznach()
print(c)

