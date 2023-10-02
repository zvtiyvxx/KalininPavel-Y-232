# -- coding: utf-8 --
n = int(input("Введите сколько прошло минут с начала суток:"))
chas = (n // 60) % 24
minutes = n % 60
print(chas,':',minutes)
#if chas < 23:
#   print(chas,':',n - chas * 60)
#elif chas > 23:
#    chas // 24 
    
