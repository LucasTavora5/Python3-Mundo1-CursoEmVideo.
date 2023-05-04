# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
m = float(input('Digite a medida em metros: '))
cm = m*100
mm = m*1000 # 1M = 100cm e 1000 mm, logo, esses são os calculos
print('{} metros convertidos ficam: {}Cm e {}Mm'.format(m,cm,mm))