# Crie um programa que leia o nome completo de uma pessoa:
nome = str(input('Digite seu nome completo: ')).strip() #.strip descarta os espaços antes e depois
# O nome com todas as letras maiúsculas
print('Seu nome todo maiúsculo: {}'.format(nome.upper()))
# O nome com todas minúsculas
print('Seu nome todo minúsculo:{}'.format(nome.lower()))
# Quantas letras tem o nome inteiro sem espacos
print('Seu nome tem ao todo {} letras sem contar os espaços'.format(len(nome)-nome.count(' '))) #len faz contar as letras, porém conta com espaços,agora, colocando -nome.coun(' ') eu descarto os espaços
# Quantas letras tem o primeiro nome:
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))# essa dica é bacana, eu uso o .find pra achar o primeiro espaço, logo, o primeiro nome.