


def solPlus():
	print('Proccess +')
	print('Enter your two number: ')
	a = int(input('a:...'))
	b = int(input('b:...'))
	print(a + b)

def solMin():
	print('Proccess -')
	print('Enter your two number: ')
	a = int(input('a:...'))
	b = int(input('b:...'))
	print(a - b)

def solUm():
	print('Proccess *')
	print('Enter your two number: ')
	a = int(input('a:...'))
	b = int(input('b:...'))
	print(a * b)

def solDe():
	print('Proccess /')
	print('Enter your two number: ')
	a = int(input('a:...'))
	b = int(input('b:...'))
	print(a / b)

def solPro():
	print('Proccess %')
	print('Enter your two number: ')
	a = int(input('a:...'))
	b = int(input('b:...'))
	print(a % b)

def sol(say):
	if say == 'plus':
		solPlus()

	elif say == 'min':
		solMin()

	elif say == '*':
		solUm()

	elif say == '/':
		solDe()

	elif say == '%':
		solPro()

	else:
		print('что-то не то')

say = str(input('What do you say?'))
sol(say)
