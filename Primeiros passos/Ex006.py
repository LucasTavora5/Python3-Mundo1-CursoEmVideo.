# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
from math import sqrt #importando a função de raíz da biblioteca de matemática
n1 = int(input('Digite um número para obter seu dobro,triplo e raíz quadrada: ')) #entrada
dobro = n1 * 2
triplo = n1 * 3 #funçoes + uso de sqrt da biblioteca de matematica
raiz = sqrt(n1)
print('O número inserido foi {},seu dobro é {},seu triplo {} e sua raíz {}'.format(n1,dobro,triplo,raiz))#saída