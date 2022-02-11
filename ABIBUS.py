import pygame
import time
import pyautogui as pg

pygame.init()  
win = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("")
bg = pygame.image.load('bg.jpg')

pygame.mixer.music.load('razeb.ogg')
pygame.mixer.music.play()

def window():

    win.blit(bg, (0, 0))

    pygame.display.update()

run = True

while run:

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    window()
    
    time.sleep(11)
    pg.alert("Ты можешь бежать, но тебе не скрыться.\n Мы повсюду.", "Сообщение от Eset")

pygame.quit()
