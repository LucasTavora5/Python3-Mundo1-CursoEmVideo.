# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
from random import choice# essa biblioteca escolhe algo aleatório de uma determinada lista, gerando diferentes resultados cada vez que for aplicada
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno:' )) # leitura de nomes
nome4 = str(input('Quarto aluno: '))
lista = [nome1,nome2,nome3,nome4] # pela primeira vez tendo um contato com listas. O [] possibilita a criação dela
escolhido = choice(lista) # escolha aleatoria da (lista)
print('A pessoa sorteada para apagar o quadro foi : {}!!!!'.format(escolhido))