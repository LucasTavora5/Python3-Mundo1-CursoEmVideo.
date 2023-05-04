'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint #randomiza um tipo INT
mix = randint(0, 5) #faz o computador escolher um numero de 0 a 5 aleatoriamente
print('Pensando em um número de 0 a 5, acha que consegue me vencer? ')
print('TENTE ADIVINHAR, HUMANO!!!')
num = int(input('Digite o número para testar o seu azar: '))
print(' tic tic tic tic tic tic tic tic tic tic...')


if num <0 :
    print('Números negativos não são permitidos, humano!!!') #condicionais!!!!
elif num >5:
    print('Números maiores que 5 não são permitidos, humano!!!')
elif num == mix:
    print('O número inserido foi {}, parabens humano, dessa vez você me venceu!!!'.format(mix))
else:
    print('Quanto azar, me desafie de novo!!!')
