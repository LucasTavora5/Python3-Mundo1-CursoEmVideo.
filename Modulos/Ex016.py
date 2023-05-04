# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc   #TRUNC  retorna a parte inteira de um número (antes da virgula)
n1 = float(input('Insira um número real: '))
print('O número digitado foi {} e sua parte inteira é {}'.format(n1,trunc(n1))) #preciso usar TRUNC no .format pra ativar a função
