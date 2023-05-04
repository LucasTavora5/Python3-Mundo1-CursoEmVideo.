# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('Digite seu nome completo: ')).strip()
n1 = nome.split() # quando faço isso crio uma lista dos nomes
print('Seu primeiro nome é {}'.format(n1[0])) # aqui puxo a posição 0 da Lista
print('Seu último nome é {}'.format(n1[len(n1)-1]))# "Len" me possibilita contar quantas unidades tem na lista -1 pois começa na posição zero