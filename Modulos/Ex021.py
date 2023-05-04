# Faça um programa em Python que abra e reproduza um arquivo mp3
'''import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
Essa forma nao funciona, aparentemente,pelo que pesquisei, a função event.wait faz ela se encerrar assim que dou play
então vou colocar outra forma da musica parar, atravez de um imput!
'''
import pygame
pygame.init() #iniciando o pygame
pygame.mixer.music.load('ex021.mp3.mp3') # dando load na música que importamos pro pycharm
pygame.mixer.music.play()# play na música
x = input('Digite algo para parar o som!!! \n') #stop
# funcionou!!