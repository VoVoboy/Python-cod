li1 = [324, 567, 78, 89]
def sol(q, w):
    if q in w:
        print('Этот эелемент есть в списке')
        print("Index: ")
        print(w.index(q))
    else:
        print('Такого елемента нет в списке')

sol(324, li1)
