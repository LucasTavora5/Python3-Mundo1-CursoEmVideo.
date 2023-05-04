# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada
dia = int(input('Informe o Dia do seu aniversário: '))#declarando as variáveis
mes = int(input('Informe o Mês do seu aniversário: '))
ano = int(input('Informe o ano dos eu aniversário: '))
print('A data do seu aniversário é {}/{}/{}'.format(dia,mes,ano))# .format coloca as variáveis na ordem das chaves