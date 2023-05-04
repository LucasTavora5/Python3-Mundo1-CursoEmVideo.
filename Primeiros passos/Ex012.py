# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preço = float(input('Digite o preço do produto: '))
desconto = preço-(preço * 5 /100) #preço comum - preço com desconto
print('O produto de preço R${:.2f}, com 5% de desconto fica em R${:.2f}'.format(preço,desconto))

