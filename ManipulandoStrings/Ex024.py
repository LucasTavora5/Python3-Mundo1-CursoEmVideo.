# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO') # esse .upper joga toda a palavra pra maiúsculoa ntes de concatenar,logo, independe a forma que eu digito
