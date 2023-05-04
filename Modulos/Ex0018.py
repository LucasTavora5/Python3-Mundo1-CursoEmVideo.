# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''from math import sin,cos,tan #importando seno,cosseno e tangente da biblioteca  de matematica
n1 = float(input('Insira um ângulo para obter seu seno,cosseno e tangente'))
print('O ângulo digitado foi {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(n1,sin(n1),cos(n1),tan(n1)))'''
import math

'''dessa forma nao funciona, preciso importar ''radians'' de math pra converter de angulo para radianos e depois calcular o valor do seno,cosseno e tang.'''
from math import sin,cos,tan,radians
ang = int(input('Insira um ângulo de 0º a 360º: '))
rad = math.radians(ang) # com isso eu converto de angulo para radianos
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang)) #variaveis de seno,cosseno e tangente se comunicando com a variavel radiano
print('O ângulo inserido foi {}, ele tem como seno {:.2f},como cosseno {:.2f} e como tangente {:.2f}'.format(ang,seno,cosseno,tangente))

#esse foi complicado, pois eu nao lembrava como fazia calculo de seno,cos, e tang e tive que pesquisar bastante