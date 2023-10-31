# -- coding: utf-8 --
def bykva(s):
    slova = s.split( )
    for slovo in slova:
        if slovo.endswith("я") or slovo.endswith("Я"):
            print(slovo)
s = input('Введите строку с несколькими словами оканчивающимися на букву я: ')
c = bykva(s)
print(c)
