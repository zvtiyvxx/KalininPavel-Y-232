# -- coding: utf-8 --
def setchikbolschemensche():
    pred = int(input('Введите целое неотрицательное число (0 для завершения): '))
    count = 0
    x = 1
    j = 1
    while pred != 0:
      x = int(input('Введите целое неотрицательное число (0 для завершения): '))
      if x == 0:
          break
      else:
          if x == pred:
              j += 1
          else:
              if j > count:
                  count = j
              j = 1
          pred = x
    if j > count:
        count = j
    return(count)
c = setchikbolschemensche()
print(c)