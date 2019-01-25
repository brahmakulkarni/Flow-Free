
import pygame
import time
import sys, os

from screen_s import *               #Importing the second screen
from game_screen_5 import *            #Importing the game screen
from game_screen_6 import *          #Importing the second screen for the level six
from screen_s_5 import *            #Importing the screen for the levels of five by five grid
from game_screen_l2 import *

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Flow Free -->>")
song = pygame.mixer.music.load("game_intro.mp3")
pygame.mixer.music.play(-1)
X = 500
Y = 500
barheight = 100                               #It is the total width of the bar 
LEFT = 1                                      #for conditions
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
###################################Third Screen#######################################

while running_i:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):                  #Event which consits of exit
            pygame.quit()
            quit()
        elif(event.type == pygame.KEYDOWN):                
            if(event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            elif(event.key == pygame.K_RETURN):
                screen_s()
    screen_i.fill((0,0,0))                                  #Filling the screen wiht black
    head1 = font_i.render("F",1,(255,0,0))                  #The font and the heading
    head2 = font_i.render("L",1,(0,255,0))
    head3 = font_i.render("O",1,(0,0,255))
    head4 = font_i.render("W",1,(255,255,0))
    head5 = font_i.render("F",1,(255,128,0))
    head6 = font_i.render("R",1,(0,0,255))
    head7 = font_i.render("E",1,(255,0,0))
    head8 = font_i.render("E",1,(0,255,0))
    screen_i.blit(head1,(120,10))                           #The placement of the  text on the screen 
    screen_i.blit(head2,(140,10))
    screen_i.blit(head3,(160,10))
    screen_i.blit(head4,(183,10))
    screen_i.blit(head5,(240,10))
    screen_i.blit(head6,(260,10))
    screen_i.blit(head7,(284,10))
    screen_i.blit(head8,(304,10))
    bln_1 = pygame.image.load("balloon_red.png")            #Placing a balloon on the screen
    bln_1 = pygame.transform.scale(bln_1,(80,80))
    bln_2 = pygame.image.load("balloon_blue.png")
    bln_2 = pygame.transform.scale(bln_2,(80,80))
    image = pygame.image.load("gameicon.png")
    screen_i.blit(image,(150,100))
    comd = font_c.render("Please press enter to continue --->>>",0,(255,255,0))
    screen_i.blit(comd,(40,450))
    screen_i.blit(bln_1,(40,350))
    screen_i.blit(bln_2,(350,40))
    clock.tick(60)
    pygame.display.flip()
        
        

