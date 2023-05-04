'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''
viagem = float(input('Será uma viagem de quantos Km?: '))
curta = 0.50 *(viagem)
longa = 0.45*(viagem)     #criei variaveis mas não precisa, eu poderia só colocar viagem *0.50 ou 0.45 antes do print
if viagem <=200:
    print('O valor a ser cobrado pra viagens com menos de 200Km é R${:.2f}'.format(curta))
else:
     print('O valor a ser cobrado por vviagens a cima de 200 km é R${:.2f}'.format(longa))