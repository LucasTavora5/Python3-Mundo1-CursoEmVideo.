# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF
c = float(input('Informe a temperatura em Celcius:'))
f = (c*1.8)+32
print('A temperatura {}ºC convertido para fahrenheit é {}ºF'.format(c,f))