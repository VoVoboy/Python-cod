def sol():

    say = str(input('What do you say?'))

    a = int(input('a:...'))
    b = int(input('b:...'))

    if say == 'plus':
    	solPlus(a, b)

    elif say == 'min':
    	solMin(a, b)

    elif say == '*':
    	solUm(a, b)

    elif say == '/':
    	solDe(a, b)

    elif say == '%':
    	solPro(a, b)

    else:
    	print('что-то не то')




def solPlus(a, b):
    print('Proccess +')
    print(a + b)

def solMin(a, b):
    print('Proccess -')
    print(a - b)

def solUm(a, b):
    print('Proccess *')
    print(a * b)

def solDe(a, b):
    print('Proccess /')
    print(a / b)

def solPro(a, b):
    print('Proccess %')
    print(a % b)

sol()
