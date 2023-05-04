# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media= (n1+n2)/2 # media aritimetica
print('A primeira nota do aluno é {}, a segunda é {}, ele obteve a média {}'.format(n1,n2,media))