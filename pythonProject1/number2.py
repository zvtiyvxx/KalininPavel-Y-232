lst = ['На входе имеем список строк разной длины', 'Необходимо написать функцию all_eq(lst)',
       'которая вернёт новый список из строк одинаковой длины.',
       'Длину итоговой строки определяем исходя из самой большой из них.']

def all_eq(lst):
    maxword = max(lst, key=len)
    for i, w in enumerate(lst):
        if w != maxword:
            l = len(maxword) - len(w)
            nw = w + l * "_"
            lst[i] = nw
    return lst

print(all_eq(lst))