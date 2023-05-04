#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Insira o primeiro segmento: '))
r2 = float(input('Insira o segundo segmento: '))
r3 = float(input('Insira o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo!!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!!')

    ### REGRA: Para formar um triângulo cada segmento tem que ser MENOR que a soma dos outros dois segmentos
    # esse foi complicado, tive que pesquisar bastante e demorei até colocar a primeira condicional dessa forma, tive que raciocinar por um bom tempo
    #aqui encerro o mundo 1 do curso em vídeo!!