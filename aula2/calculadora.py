#!/usr/bin/python3

import sys

print(sys.argv)

for k in range(len(sys.argv)):
	print('Parametro {}: {}'.format(k,sys.argv[k]))

exit()
#calculadora com ARGS

def descobre_dic (**kwargs):
	print(kwargs)

	for k in kwargs.keys():
		print('chave: {}'.format(k))
		print('valor: {}'.format(kwargs[k]))

descobre_dic(nome="servidor",ip="192.168.16.1",
	dominio="4linux.com.br")
print("\n")

descobre_dic(user="joaozinho",nome="joao",sobrenome = "silva", 
	idade = "20")

exit()

#gabarito professor calculadora simples

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
