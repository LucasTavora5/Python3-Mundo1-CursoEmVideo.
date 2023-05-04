# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele
entrada = input('Digite uma palavra para saber seu tipo primitivo: ')
print("Tipo primitivo: {}.".format(type(entrada))) #type= função para saber o tipo de algo

print("É numérico? {}".format(entrada.isnumeric()))
print("É alfanumérico? {}.".format(entrada.isalpha())) # dessa forma irei obter True or False no prompt
print("É um decimal? {}.".format(entrada.isdecimal()))
print("Está em caixa baixa? {}.".format(entrada.islower()))
print("É apenas espaço em branco? {}.".format(entrada.isspace()))
print("Está em caixa alta? {}.".format(entrada.isupper()))
