#!/usr/bin/python3

#dicionario

herois = {'batman':{'identidade':'bruce wayne','cidade':'gotham'},
'superman':{'identidade':'clark kent','cidade':'metropolis'}}

print(herois['batman']['identidade'])

lanche = {'pao': ['integral','4queijos','italiano'],
'queijo':['prato','chedar','suico'],
'recheio': ['frango','carne','almondega']}
print(lanche['pao'][2])

exit()


koppa1 = {'cor':'vermelho', 'pontos' : 30}
koppa2 = {'cor':'verde', 'pontos' : 50}
koppa3 = {'cor':'azul', 'pontos' : 100}

koppa = [koppa1,koppa2,koppa3]
print(koppa[1]['cor'])

lista = []

for k in range (10):
	lista.append(koppa1)


usuario = {'username' : 'exemplo1' , 'nome' : 'joao' ,
 'sobrenome' : 'silva'}

print(usuario)
for chave,valor in usuario.items():
	print('chave: {}'.format(chave))
	print('valor: {}'.format(chave))

for chave in usuario.keys():
	print('chave: {}'.format(chave))

for valor in usuario.values():
	print('valor: {}'.format(valor))

exit()

#conceito dicionario

cores = {'red':'vermelho', 'blue': 'azul' , 'green': 'verde'}
#print(cores['red'])

koppa1 = {'cor': 'vermelho' , 'pontos' : 30}

pontos = koppa1['pontos']
#print (pontos)

koppa1['eixo_x'] = 5
koppa1 ['eixo_y'] = 15
koppa1 ['velocidade'] = 'rapido'

print(koppa1)

if koppa1['velocidade'] == 'lento':
	anda_x = 1
elif koppa1['velocidade'] == 'medio':
	and_x = 2
else:
	anda_x = 3

koppa1['eixo_x'] += anda_x

print(koppa1)
exit()


#conceito Tupla

retangulo = (100,50)
print(retangulo[0],retangulo[1])
# retangulo[0] = 30
retangulo = (30,50)
print(retangulo[0],retangulo[1])
x = list (retangulo)
x [0] = 300
print (x)

exit()


#lista

#pot = []

#for valor in range (1,11):
#	if valor% 2 == 0:		
#		pot.append(valor)
#print(pot)
#exit()

pot = [valor for valor in range (1,11)
		if valor % 2 == 0]
print(pot)
exit()