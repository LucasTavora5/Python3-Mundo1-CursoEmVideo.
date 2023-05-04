# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
distancia = float(input('Informe a distancia da viagem em Km: '))
tempo = int (input('Informe a quantidade de dias do aluguel: '))
diaria = (60 * tempo)+(0.15 *distancia)
print('O aluguel do carro por {} dias e com {} Km rodados fica em R${}'.format(tempo,distancia,diaria))


