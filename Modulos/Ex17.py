# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''a = float(input('Insita o comprimento do cateto oposto: '))
b = float(input('Insira o comprimento do cateto adjacente: '))
hipotenusa = (a*2)+(b*2)
print('O triângulo com cateto oposto {} e cateto adjacente {} tem a hipotenusa {}'.format(a,b,hipotenusa))
 eu deveria ter importado ao menos a função Sqrt da biblioteca math pra isso dar certo, pois precido saber
  a raiz quadrada de A²+B²'''

#agora farei utilizando a biblioteca de matematica com função hipotenusa
from math import hypot
co = float(input('Informe o cateto oposto:'))
ca= float(input('Informe o cateto adjacente:'))
hypot(co,ca)
print('O triangulo com cateto oposto {} e cateto adjacente {} tem como hipotenusa {:.2f}'.format(co,ca,hypot(co,ca)))