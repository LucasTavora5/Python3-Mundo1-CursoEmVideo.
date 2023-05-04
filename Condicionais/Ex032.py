#$Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO


'''year = int(input('Digite um ano para saber se ele é bissexto: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Esse é um ano bissexto!')
else:
    print('Esse não é um ano bissexto')'''
    #####EXTRA####
    #coloque 1 para saber se o ano atual é BISSEXTO
from datetime import date
year = int(input('Para saber do ano atual basta digitar o número "0"\nDigite um ano para saber se ele é bissexto: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #ano bissexto é divisivel por 4 exceto os múltiplos de 100 que não são múltiplos de 400
        print('O ano {} é um ano bissexto'.format(year))
else:
        print('O ano {} não é um ano bissexto'.format(year))
