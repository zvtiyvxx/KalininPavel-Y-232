# -- coding: utf-8 --
def setchikbolschemensche():
    pred = int(input('Введите целое неотрицательное число (0 для завершения): '))
    count = 0
    x = 1
    while pred != 0:
      x = int(input('Введите целое неотрицательное число (0 для завершения): '))
      if x == 0:
          break
      else:
          if x > pred:
              count += 1
      pred = x
    return(count)
c = setchikbolschemensche()
print(c)
