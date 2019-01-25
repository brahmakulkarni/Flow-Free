import pygame
import time
import sys
import os


from game_screen_5 import *
from game_screen_l2 import *
from game_screen_6 import *
from game_screen_6_l2 import *
from screen_s import *


pygame.init()
pygame.display.set_caption("Flow Free -->>")
X = 500
Y = 500
barheight = 100                               #It is the total width of the bar 
LEFT = 1                                      #for conditions
song_s = pygame.mixer.music.load("game_intro.mp3")
screen_i = pygame.display.set_mode((X,Y));    #For the introduciton screen
borcolor = []
running_i= True
for i in range(1,63):
    borcolor.append((0,0,i * 4))
bgheight = 50                                               #The width of the border
font = pygame.font.SysFont("Century Schoolbook L" , 18)     #Font style setting
font_i = pygame.font.SysFont("URW Palladio L",50)
font_c = pygame.font.SysFont("Monospace",20)
font_l = pygame.font.SysFont("Monospace",30)

def screen_s_6():
    screen_s_6 = pygame.display.set_mode((X,Y))
    running = 1
    while running:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_1 or event.key == pygame.K_KP1):
                    pygame.mixer.music.stop()
                    game_screen_6()
                elif(event.key == pygame.K_2 or event.key == pygame.K_KP2):
                    pygame.mixer.music.stop()
                    game_screen_6_l2()
                elif(event.k,ey == pygame.K_b):
                    return 
                    pygame.display.update()
        screen_s_6.fill((0,0,0)) 
        head1_s = font_i.render("L",1,(255,0,0))
        head2_s = font_i.render("e",1,(0,255,0))
        head3_s = font_i.render("v",1,(0,0,255))
        head4_s = font_i.render("e",1,(255,255,0))
        head5_s = font_i.render("l",1,(255,128,0))
        head6_s = font_i.render("s",1,(0,0,255))
        screen_s_6.blit(head1_s,(180,10))
        screen_s_6.blit(head2_s,(200,10))
        screen_s_6.blit(head3_s,(220,10))
        screen_s_6.blit(head4_s,(240,10))
        screen_s_6.blit(head5_s,(260,10))
        screen_s_6.blit(head6_s,(270,10))
        five_l = font_l.render("Level - 1",0,(255,0,0))
        six_l = font_l.render("Level - 2",0,(0,255,0))
        screen_s_6.blit(five_l,(160,200))
        screen_s_6.blit(six_l,(160,240))
        di = font_c.render("Press the number to go to the respective level",1,(0,0,255))
        screen_s_6.blit(di,(10 ,450))
        pygame.display.flip()   
