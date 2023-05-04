# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Sem usar estruturas de repetição, pois ainda nao aprendi!!!

num = int(input('Digite um número: '))
u = num // 1 %10 #divide por 1 =  ele mesmo, divide por 10 e pega o resto, tenho a unidade!
d = num // 10 %10 #divide por 10 e pega o resto, tenho a dezena e assim sucessivamente
c = num // 100 %10 #matematica basica de dezena, centena e milhar, esse resto de 10 me faz ter só a casa decimal que eu quero
m = num // 1000 %10
print('Analisando o número {}.....'.format(num))
print('Unidade:{}'.format([u]))
print('Dezena: {}'.format([d]))
print('Centena:{}'.format([c]))
print('Milhar:{}'.format([m]))