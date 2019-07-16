#!/usr/bin/python3


#alterar vogais por asterisco
#jeito 1

palavra = input('Digite Palavra: ')

vogais = 'aeiou'
troca = ''

for k in palavra:
	if k in vogais:
		troca += '*'
	else:
		troca += k

print(troca)
exit()


#jeito 2

vogais = 'aeiouAEIOUáéíóúÂÊÎÔÛ'
palavra = input('Digite Palavra: ')
for k in palavra:
	if k in vogais:
		palavra = palavra.replace(k,'*')

print(palavra)

exit()


#como detectar se uma palavra é palindromo

palavra = input('Digite uma Palavra: ')

if palavra == palavra[:: -1]: #[:: -1] este é o comando para a variavel ao contrario

	print (palavra + ' é palíndromo')
else:
	print (palavra + ' não é palíndromo')


exit()


