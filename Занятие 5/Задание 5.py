# -- coding: utf-8 --
def setchik():
    count = 0
    x = 1
    while x != 0:
      x = int(input('Введите целое неотрицательное число (0 для завершения): '))
      if x == 0:
        break  
      else:
        count += 1
    return(count)
c = setchik()
print(c)
