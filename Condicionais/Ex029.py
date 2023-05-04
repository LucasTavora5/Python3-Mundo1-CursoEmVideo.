''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
'''
speed = float (input('Insira aqui a velocidade atingida em Km: ')) #entrada de dados
multa = 7.00 *(speed-80) # *(speed-80) faz com que eu multiplique o valor 7 pela velocidade -80 que é o limite
if speed <= 80:
    print('Não há multas a serem cobradas')
else:
    print('Você recebeu uma multa no valor de R${:.2f}'.format(multa)) #nao usei elif por serem apenas duas condições, se nao atender if...então fazer else.

