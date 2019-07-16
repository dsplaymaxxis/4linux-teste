#!/usr/bin/python3


def soma(a,b):
	return a + b
def sub(a,b):
	return a - b
def mult(a,b):
	return a * b
def divisao(a,b):
	return a / b



operadores = '+-*/'
operacao = input('Digite : ')

for k in operacao:
	if k in operadores:
		o = k
		a,b = operacao.split(k)
		a = int(a)
		b = int(b)

dic = {'+': soma, '-' : sub,'*': mult,'/' : divisao}

z = dic[o](a,b)
print(z)
# if k == '+'
# 	print(a+b)
# elif k == '-'
# 	print(a-b)
# elif k == '*'
# 	print(a*b)
# elif k == '/'
# 	print(a/b)


exit()



#calculadora feito por elder


a1 = int(input('Digite um numero : ' ))
a2 = input('Digite uma operação matematica (+-/*) :')
a3 = int(input('Digite outro numero : '))

def soma():
	a = format(a1 + a3)  
	return(a)

def sub():
	b = format(a1 - a3)  
	return(b)

def multi():
	c = format(a1 * a3)  
	return(c)

def div():
	d = format(a1 / a3)  
	return(d)

if a2 == '+':
	print('O Resultado é : ' + soma())
elif a2 == '-':
	print('O Resultado é : ' + sub())
elif a2 == '*':
	print('O Resultado é : ' + multi())
elif a2 == '/':
	print('O Resultado é : ' + div())

exit()





exit()
#funcoes



def calcular_fig_geometrica(*args):
	if len(args) == 1:
		print('Area do quadrado: {}'
			.format(args[0]**2))
	elif len (args) == 2:
		print('Area do retangulo: {}'
			.format(args[0]*args[1]))
	else:
		print('Volume: {}'
			.format(args[0]*args[1]*args[2]))

calcular_fig_geometrica(2)
calcular_fig_geometrica(2,10)
calcular_fig_geometrica(2,10,10)
exit()

			


def animal(tipo='cachorro',nome='rex'):
	print ('eu tenho um {} que se chama {}'
		.format(tipo.nome))

#animal('cachorro','rex')
exit()

def diga_ola(n):
	print('ola' + n)

#nome = 'pedro'
#diga_ola (nome)

def pergunta():
	nome = input('digite nome: ')
	return nome

x = pergunta()
diga_ola(x)


exit()
def diga_ola():
	print('ola')

diga_ola()