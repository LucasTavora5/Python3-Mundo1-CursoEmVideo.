# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
b = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = b * h #calculo de area
tinta = a / 2 #dividido por 2, pois 1 galao pinta 2m²
print('uma parede com {:.2f}M de largura e {:.2f}M de altura tem a área de {}.\nA quantidade de tinta necessária é de {}L'.format(b,h,a,tinta))
#quando uso {:.2f} deixo 2 casas decimais depois da virgula