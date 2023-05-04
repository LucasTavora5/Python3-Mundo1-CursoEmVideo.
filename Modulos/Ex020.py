# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle # a subclasse Shuffle embaralha elementos de uma lista
a1 = input('Primeiro aluno: ') #quando nao declaro o tipo de variável ele entende como String
a2 = input('Segungo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1,a2,a3,a4] #criação da lista
shuffle(lista) #função shuffle sendo aplicada
print('A ordem de escolha para a a apresentação será {}'.format(lista))