'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.'''
salario = float(input('Informe aqui seu salário para saber o reajuste: R$'))
a1 = salario + (salario*10 / 100)
a2 = salario + (salario*15 / 100)
if salario >1250:
    print('O salário R${:.2f} teve o reajuste de mais 10% e passa a ser R${:.2f}'.format(salario,a1))
if salario <=1250:
    print('O salário R${:.2f} teve o reajuste de mais 15% e passa a ser R${:.2f}'.format(salario,a2))