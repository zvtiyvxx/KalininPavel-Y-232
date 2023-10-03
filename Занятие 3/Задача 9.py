# -- coding: utf-8 --
def chokoladka(n,m,k):
    if ((m // 2) * n) == k:
        return('Да')
    else:
        return('Нет')
n = int(input('Введите колличество (длину шоколадки) долек '))
m = int(input('Введите колличество (ширину шоколадки) долек '))
k = int(input('Введите сколько долек должно остаться (отломить можно только пополам, по ширине) '))
c = chokoladka(n,m,k)
print(c)

