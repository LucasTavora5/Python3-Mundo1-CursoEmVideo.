#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n1 = int(input('Insira um número inteiro para saber se é par ou ímpar: '))
if n1 %2 == 0:                                       # se o resto da divisão de n1 for exatamente 0, ele é par
    print('O {} é um número  par'.format(n1))
else:
    print('O {} é um número ímpar!'.format(n1))      #senão, é ímpar!