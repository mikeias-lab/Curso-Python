import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
print('Musica carregada com sucesso')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)