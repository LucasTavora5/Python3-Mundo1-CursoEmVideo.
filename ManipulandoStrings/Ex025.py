# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome =  str(input('Digite o nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())) # operador "In" pra saber se contém ou nao contém e mais uma vez jogando pra .upper antes de concatenar