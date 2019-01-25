import pygame
from game_screen_5 import *
from screen_s import *
#from code import *

X = 500
Y = 500
font_my = pygame.font.SysFont("Monospace",15)
def help_screen():
    help_screen = pygame.display.set_mode((X,Y))
    running = 1
    while(running):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_b):
                    return
                    pygame.display.update()
        help_screen.fill((0,0,0))
        rl = font_i.render("Rules",1,(255,255,0))
        x1 = "The player is given a grid with dots of"
        y1 = "different colors. "
        x2 = "The player has to join the dots of the same"
        y2 = "color in such a way that each of the lines dose" 
        y22 = "not cross the other "      
        x3 = "In the present game the controls are the"
        y3 = "keyboard for the menu." 
        x4 = "The player can connect the dots using the mouse."
        x5 = "If the user uses the wrong direction the line" 
        y5 = "wont'be shown which is a sign of an error." 
        x6 = "The player shouldn't leave any of the grids empty."
        rl1 = font_my.render("1.  "+str(x1),1,(255,0,0))
        rl11 = font_my.render("   "+str(y1),1,(255,0,0))
        rl2 = font_my.render("2. "+str(x2),1,(0,0,255))
        rl22 = font_my.render("   "+str(y2),1,(0,0,255))
        rl222 = font_my.render("   "+str(y22),1,(0,0,255))
        rl3 = font_my.render("3. "+str(x3),1,(0,255,0))
        rl33 = font_my.render("   "+str(y3),1,(0,255,0))
        rl4 = font_my.render("4. "+str(x4),1,(255,128,0))
        rl5 = font_my.render("5. "+str(x5),1,(0,128,255))
        rl55 = font_my.render("   "+str(y5),1,(0,128,255))
        rl6 = font_my.render("6. "+str(x6),1,(255,127,0))
        help_screen.blit(rl,(230,80))
        help_screen.blit(rl6,(30,395))
        help_screen.blit(rl1,(30,175))
        help_screen.blit(rl11,(30,190))
        help_screen.blit(rl2,(30,225))
        help_screen.blit(rl22,(30,240))
        help_screen.blit(rl222,(30,255))
        help_screen.blit(rl3,(30,280))
        help_screen.blit(rl33,(30,295))
        help_screen.blit(rl4,(30,320))
        help_screen.blit(rl5,(30,350))
        help_screen.blit(rl55,(30,365))
        pygame.display.flip()
