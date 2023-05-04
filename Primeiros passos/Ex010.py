# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
dinheiro = float(input('insira a quantidade em reais: '))
dolar = 5.07 #Cotação 10/04/2023
conversão = dinheiro/5.07
print('Com R${:.2f}, voce consegue comprar ${:.2f} (Dólares)'.format(dinheiro,conversão))
