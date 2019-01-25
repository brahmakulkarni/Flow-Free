import pygame
import time
import sys
import os
pygame.init()
X = 500
Y = 500
clock = pygame.time.Clock()
font_h = pygame.font.SysFont("Purisa",70)
def game_over():
    game_over = pygame.display.set_mode((X,Y))
    running = 1
    while(running):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    quit()
                elif(event.key == pygame.K_RETURN):
                    game_screen_l2()
        game_over.fill((0,0,0))
        g = font_h.render("Y",0,(0,0,255))
        a = font_h.render("O",0,(255,0,0))
        m = font_h.render("U",0,(255,0,127))
        o = font_h.render("W",0,(128,255,0))
        v = font_h.render("O",0,(0,204,204))
        e = font_h.render("N",0,(0,255,0))
        r = font_h.render("!",0,(255,127,0))
        game_over.blit(g,(100,200))
        game_over.blit(a,(150,200))
        game_over.blit(m,(200,200))
        game_over.blit(o,(300,200))
        game_over.blit(v,(350,200))
        game_over.blit(e,(400,200))
        game_over.blit(r,(450,200))
        clock.tick(60)
        pygame.display.flip()


