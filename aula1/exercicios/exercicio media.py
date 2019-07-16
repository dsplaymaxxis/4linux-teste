#!/usr/bin/python3  
#para escolher a versao do python


#
#calcular media 2


nome = input('Digite Nome: ')
N1 = float(input('Digite Nota: '))
N2 = float(input('Digite Nota: '))
N3 = float(input('Digite Nota: '))
N4 = float(input('Digite Nota: '))

media = ((N1+N2+N3+N4)/4)

if media >= 7: 
	print(nome + ' obteve media igual a  ' + str(media) + ' = Aprovado')
elif media >= 5 and media <= 7 :
	N5 = float(input('Digite Nota: '))
	media2 = ((media + N5)/2)
	if media2 >= 5:
		print(nome + ' obteve media igual a  ' + str(media2) + ' = Aprovado')
	else:
		print(nome + ' obteve media igual a  ' + str(media2) + ' = Reprovado')	
else: 
	print(nome + ' obteve media igual a  ' + str(media) + ' = Reprovado')
exit()



# Abaixo de 200min cobra R$ 0.20 por min
# Entre 200 e 400 min cobra R$ 0.18
# Acima de 400 o preco e R$ 0.15

minutos = int(input('minutos utilizados : '))

if minutos < 200:
	preco = 0.2
elif minutos <= 400:
	preco = 0.18
else:
	preco = 0.15

	print('conta: R$ {:.2f}'.format(minutos * preco)) 
exit()


#multa velocidade

idade = int(input('Digite idade: '))
Habilitacao = input('possui habilitacao: ')
h = False

if habilitacao.lower().strip() == 'sim' :
	h = True
if idade >= 18 and h == True:
	print('Pode dirigir')
else:
	print('Nao pode dirigir')

exit()
velocidade = int(input('Digite Vel.: '))

if velocidade > 110:
	multa = (velocidade - 110) * 5
	print('multa: R${:.2f}'.format(multa))




#calcular media


nome = input('Digite Nome: ')
N1 = float(input('Digite Nota: '))
N2 = float(input('Digite Nota: '))
N3 = float(input('Digite Nota: '))
N4 = float(input('Digite Nota: '))

media = ((N1+N2+N3+N4)/4)

if media > 7: 
	print(nome + ' obteve media igual a  ' + str(media) + ' = Aprovado')

else: 
	print(nome + ' obteve media igual a  ' + str(media) + ' = Reprovado')
exit()

