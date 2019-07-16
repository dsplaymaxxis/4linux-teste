#!/usr/bin/python3  
#para escolher a versao do python

herois = ['superman2','batman','flash',
'mulher maravilha','robin','thor']

heroi = 'capitao america'

if heroi in herois:
	print ('ta na lista')
else:
	print ('o heroi ' + heroi + ' nao ta na lista')

for heroi in herois:
	print(heroi)

exit()


valor = list(range(2,15))

print(valor)
soma = 0
n = 0
while n < len(valor):
	soma += valor[n]
	n += 1
print("Media {}".format(soma / len(valor))) 

exit()


herois = ['superman2','batman','flash','mulher maravilha','robin','thor']
print(herois,len(herois))
herois[2] = 'arqueiro verde'
print(herois,len(herois))
herois.insert(2,'robin')
print(herois,len(herois))
del herois[0]
print(herois.len(herois))
pop_herois.len(herois)