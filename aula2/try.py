#!/usr/bin/python3


#arquivo  estudar como funciona arquivo no python
arq = 'arquivo.txt'

nomes = ['Robin\n' , 'Mulher Maravilha\n', 'Superman\n']

with opewn(arq,"a") as arquivo:
	arquivo.writelines(nomes)

with open(arq) as arquivo:
	conteudo = arquivo.read()
	print(conteudo)

exit()

arq = 'arquivo.txt'

with open(arq,"w") as arquivo:
	arquivo.write('Batman\n')

exit()

with open('arquivo.txt') as arquivo:
	linhas = arquivo.readlines()
print(linhas)

exit()

with open('arquivo.txt') as arquivo:
	for linha in arquivo:
		print(linha)
exit()



with open ('arquivo.txt') as arquivo:
	conteudo = arquivo.read()
	print(conteudo)


exit()
arquivo = open('arquivo.txt',"r")
print(arquivo.read())
arquivo.close()

exit()

#Recurso Try e Break
while True:

	try:
		n1 = int(input("Digite: "))
		n2 = int(input("Digite: "))
		r = n1/n2
	except ZeroDivisionError as e:
		print("Impossivel dividir por Zero!")
	except NameError as e:
		print("Variavel inexistente")
	except ValueError as e:
		print("Digite numeros!")
		break
	else:
		print(r)

exit()

try:
	print(5/0)
except ZeroDivisionError as e:
	print("Erro: {}".format(e))