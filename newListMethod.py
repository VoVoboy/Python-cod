l1 = [34, 78, 90, 45678]


def repli(q, w):
    a = w.index(q)
    b = w.count(q)
    
    li = [a, b]
    
    if q in w:
        print('Выполение методов из созданного списка')
        for z in li:
            print('Внесены изменения')
            print(z)
    else:
        print('нет совпадающих элементов в списке')
repli(45678, l1)
