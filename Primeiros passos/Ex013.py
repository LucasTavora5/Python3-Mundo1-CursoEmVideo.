# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Informe seu salário para calcular o aumento: \nR$')) #entrada
aumento = salario+(salario*15/100) #como é acréscimo soma, se fosse desconto diminuiria #processamento
print('O salário de R${:.2f} com um aumento de 15% fica em R${:.2f}'.format(salario,aumento))#saída
