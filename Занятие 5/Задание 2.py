# -- coding: utf-8 --
def delitel(N):
    if N > 2:
        i = 2
        while i <= N:
            if N % i == 0:
                return(i)
            else:
                i += 1
    else:
        return (print('Введите число больше 2!'))
N = int(input('Введите целое число:'))
c = delitel(N)
print(c)