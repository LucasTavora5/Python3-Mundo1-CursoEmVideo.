#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1             #declara n1 como o menor e ja descarta um if
if n2 < n1 and n2 < n3:
    menor = n2                 # se n2 for menor que n1 e que n3, então ele é o menor e assim por diante
if n3 < n2 and n3 < n1:
    menor = n3

    maior = n1         #declara n1 como maior e ja descarta um if
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
    print('O maior valor entre os três números é {}'.format(maior))
    print('O menor valor entre os três números é {}'.format(menor))


