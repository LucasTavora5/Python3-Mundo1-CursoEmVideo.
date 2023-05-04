# Faça um programa que leia uma frase qualquer e mostre:
frase = str(input('Digite uma frase: ')).strip().upper()
# Quantas vezes aparece a letra "a"

print('A letra "A" aparece {} vezes'.format(frase.count('A')))# count conta o total de vezes que um elemento aparece e graças ao Upper no inicio, consegui padronizar pros minusculos
# Em que posição ela aparece a primeira vez
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')))#find procura da esquerda pra direita
# Em que posição ela aparece a última vez
print('A ultima letra "A" apareceu na posição {}'.format(frase.rfind('A')))#rfind procura da direita pra esquerda


