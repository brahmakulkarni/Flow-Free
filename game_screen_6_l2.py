import pygame
import sys
import time
import os

pygame.init()
pygame.display.set_caption("Flow Free -->>")
X = 550
Y = 550
from game_over import *
RED = (255,0,0)
GREEN = (50,205,50)
BLUE = (0,0,205)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
#global variables
circ = 0
r2a = 175
r2b = 225
r2c = 225
r2d = 275
r2e = 275
r2f = 325
r2g = 225
r2h = 275
g2a = 175
g2b = 225
g2c = 325
g2d = 375
g2e = 325
g2f = 375
g2g = 325
g2h = 375
g2i = 325
g2j = 375
g2k = 325
g2l = 375
b2a = 175
b2b = 225
b2c = 275
b2d = 325
y2a = 325
y2b = 375
y2c = 325
y2d = 375
o2a = 125
o2b = 175
o2c = 325
o2d = 375
o2e = 175
o2f = 225
o2g = 175
o2h = 225
o2i = 225
o2j = 275
o2k = 275
o2l = 325
o2m = 175
o2n = 225
o2o = 225
o2p = 275
o2q = 175
o2r = 225
o2s = 175
o2t = 225
flow = 0
done2_r = 0
done2_g = 0
done2_b = 0
done2_y = 0
done2_o = 0

barheight = 100                         #It is the total width of the bar
LEFT = 1                                 #for conditions
borcolor = []
for i in range(1,63):
    borcolor.append((0,0,i * 4))
bgheight = 50                                               #The width of the border
font = pygame.font.SysFont("Century Schoolbook L" , 18)     #Font style setting
font_i = pygame.font.SysFont("URW Palladio L",50)
font_c = pygame.font.SysFont("Monospace",20)
font_l = pygame.font.SysFont("Monospace",30)

def game_screen_6_l2():
    global circ
    global r2a
    global r2b
    global r2c
    global r2d
    global r2e
    global r2f
    global r2g
    global r2h
    global g2a
    global g2b
    global g2c
    global g2d
    global g2e
    global g2f
    global g2g
    global g2h
    global g2i
    global g2j
    global g2k
    global g2l
    global b2a
    global b2b
    global b2c
    global b2d
    global y2a
    global y2b
    global y2c
    global y2d
    global o2a
    global o2b
    global o2c
    global o2d
    global o2e
    global o2f
    global o2g
    global o2h
    global o2i
    global o2j
    global o2k
    global o2l
    global o2m
    global o2n
    global o2o
    global o2p
    global o2q
    global o2r
    global o2s
    global o2t
    global flow
    global done2_r
    global done2_g
    global done2_b
    global done2_y
    global done2_o



    screen_6_l2 = pygame.display.set_mode((X,Y))
    running = 1                                 #This is for the condition in the while loop
    while running:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    quit()
                elif(event.key == pygame.K_b):
                    flow = 0
                    return
                    pygame.display.update()
   #Iteration for horizontal lines
        y = 125                                                 #starting point
        while(y <= 425):
            pygame.draw.line(screen_6_l2 , (255 , 153 , 153) , (125 , y) , (425,y))   #code for line from one co-ordinate to another
            y += 50                             #increasing 40 for each iteration because the width of each is 40
        x = 125                                   #Variable for vertical lines

    #Iteration for vertical lines
        while(x <= 425):
            pygame.draw.line(screen_6_l2 , (255,153,153) , (x,125) , (x , 425))
            x += 50
    #Drawing coloured circles
        pygame.draw.circle(screen_6_l2, RED, (250,200), 20)
        pygame.draw.circle(screen_6_l2, GREEN, (400, 150), 20)
        pygame.draw.circle(screen_6_l2, BLUE, (350, 150), 20)
        pygame.draw.circle(screen_6_l2, GREEN, (300, 300), 20)
        pygame.draw.circle(screen_6_l2, YELLOW, (250, 300), 20)
        pygame.draw.circle(screen_6_l2, YELLOW, (250, 400), 20)
        pygame.draw.circle(screen_6_l2, BLUE, (350, 350), 20)
        pygame.draw.circle(screen_6_l2, RED, (200, 350), 20)
        pygame.draw.circle(screen_6_l2, ORANGE, (200, 400), 20)
        pygame.draw.circle(screen_6_l2, ORANGE, (250, 250), 20)
    #Vertical Borders
        x = 0
        while(x < bgheight):
            pygame.draw.line(screen_6_l2 , borcolor[x] , ((40 - x),0) , ((40 - x) , Y))
            x += 1
        x = 0
        while(x <  bgheight):
            pygame.draw.line(screen_6_l2 , borcolor[x] , ((X - 40) + x , 0) , ((X - 40) + x , Y))
            x += 1
    #Horizontal Borders
        y = 0
        while(y < bgheight):
            pygame.draw.line(screen_6_l2 , borcolor[y] , (30, (40 - y)) , (X - 30 ,(40 - y)))
            y += 1
        y = 0
        while(y < bgheight):
            pygame.draw.line(screen_6_l2 , borcolor[y] , (30 , (Y-40) + y) , (X - 30,(Y - 40) + y))
            y += 1

        label = font.render("Flows :" , 0 , (255,255,255))
        screen_6_l2.blit(label,(130,110))
        label1 = font.render("Level - 2" , 0 ,(255,255,255))
        screen_6_l2.blit(label1,(240,110))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                    pygame.quit()
            if e.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                mx , my = pygame.mouse.get_pos()
                #deciding colour based on mouse position
                if ((mx in range(225,275) and my in range(175,225)) or (mx in range(175,225) and my in range(325,375))):
                    circ = 1 #RED
                elif ((mx in range(375,425) and my in range(125,175)) or (mx in range(275,325) and my in range(275,325))):
                    circ = 2 #GREEN
                elif ((mx in range(325,375) and my in range(125,175)) or (mx in range(325, 375) and my in range(325, 375))):
                    circ = 3 #BLUE
                elif ((mx in range(225,275) and my in range(275,325)) or (mx in range(225,275) and my in range(375,425))):
                    circ = 4 #YELLOW
                elif ((mx in range(175,225) and my in range(375,425)) or (mx in range(225,275) and my in range(225,275))):
                    circ = 5 #ORANGE

                if (circ == 1):
                    if (mx in range(r2a,r2b) and my in range(175,225)):
                        pygame.draw.line(screen_6_l2, RED, (r2b + 25, 200), (r2a + 16, 200), 20)
                    elif (mx in range(175,225) and my in range(r2c,r2d)):
                        pygame.draw.line(screen_6_l2, RED, (200, r2c - 34), (200, r2d-25), 20)
                        if (my not in range(325, 375)):
                            r2c += 50
                            r2d += 50
                        else:
                            if (done2_r == 0):
                                done2_r = 1
                                flow += 1
                            continue
                    if (mx in range(175,225) and my in range(r2e,r2f)):
                        pygame.draw.line(screen_6_l2, RED, (200, r2f + 25), (200, r2e + 25), 20)
                        if (my not in range(175,225)):
                            r2e -= 50
                            r2f -= 50
                        else:
                            continue
                    elif (mx in range(r2g,r2h) and my in range(175,225)):
                        pygame.draw.line(screen_6_l2, RED, (200, r2g - 34), (200, r2h - 25), 20)
                        if (done2_r == 0):
                            done2_r = 1
                            flow += 1
                elif (circ == 2):
                    if (mx in range(375,425) and my in range(g2a, g2b)):
                        pygame.draw.line(screen_6_l2, GREEN, (400, g2a - 25), (400, g2b - 25), 20)
                        if (my not in range(375,425)):
                            g2a += 50
                            g2b += 50
                        else:
                            continue
                    elif (mx in range(g2c,g2d) and my in range(375,425)):
                        pygame.draw.line(screen_6_l2, GREEN, (g2d + 34, 400), (g2c + 25, 400), 20)
                        if (mx not in range(275,325)):
                            g2c -= 50
                            g2d -= 50
                        else:
                            continue
                    elif (mx in range(275,325) and my in range(g2e,g2f)):
                        pygame.draw.line(screen_6_l2, GREEN, (300, g2f + 34), (300, g2e + 25), 20)
                        if (my not in range(275,325)):
                            g2e -= 50
                            g2f -= 50
                        else:
                            if (done2_g == 0):
                                done2_g = 1
                                flow += 1
                            continue
                    if(mx in range(275,325) and my in range(g2g,g2h)):
                        pygame.draw.line(screen_6_l2, GREEN, (300, g2g -25), (300, g2h -25), 20)
                        if (my not in range(375,425)):
                            g2g += 50
                            g2h += 50
                        else:
                            continue
                    elif (mx in range(g2i,g2j) and my in range(375,425)):
                        pygame.draw.line(screen_6_l2, GREEN, (g2i - 34, 400), (g2j - 25, 400), 20)
                        if (mx not in range(375,425)):
                            g2i += 50
                            g2j += 50
                        else:
                            continue
                    elif (mx in range(375,425) and my in range(g2k, g2l)):
                        pygame.draw.line(screen_6_l2, GREEN, (400, g2l + 34), (400, g2k + 25), 20)
                        if (my not in range(125,175)):
                            g2k -= 50
                            g2l -= 50
                        else:
                            if (done2_g == 0):
                                done2_g = 1
                                flow += 1
                            continue
                elif (circ == 3):
                    if (mx in range(325,375) and my in range(b2a,b2b)):
                        pygame.draw.line(screen_6_l2, BLUE, (350, b2a - 25), (350, b2b - 25), 20)
                        if (my not in range(325,375)):
                            b2a += 50
                            b2b += 50
                        else:
                            if (done2_b == 0):
                                done2_b = 1
                                flow += 1
                            continue
                    if (mx in range(325,375) and my in range(b2c,b2d)):
                        pygame.draw.line(screen_6_l2, BLUE, (350, b2d + 25), (350, b2c + 25), 20)
                        if (my not in range(125,175)):
                            b2c -= 50
                            b2d -= 50
                        else:
                            if (done2_b == 0):
                                done2_b = 1
                                flow += 1
                            continue
                elif (circ == 4):
                    if (mx in range(225,275) and my in range(y2a,y2b)):
                        pygame.draw.line(screen_6_l2, YELLOW, (250, y2a - 25), (250, y2b - 25), 20)
                        if (my not in range(375,425)):
                            y2a += 50
                            y2b += 50
                        else:
                            if (done2_y == 0):
                                done2_y = 1
                                flow += 1
                            continue
                    if (mx in range(225,275) and my in range(y2c,y2d)):
                        pygame.draw.line(screen_6_l2, YELLOW, (250, y2d + 25), (250, y2c + 25), 20)
                        if (my not in range(275,325)):
                            y2a += 50
                            y2b += 50
                        else:
                            if (done2_y == 0):
                                done2_y = 1
                                flow += 1
                            continue
                elif (circ == 5):
                    if (mx in range(o2a,o2b) and my in range(375,425)):
                        pygame.draw.line(screen_6_l2, ORANGE, (o2b + 25, 400), (o2a + 16, 400), 20)
                    elif (mx in range(125,175) and my in range(o2c,o2d)):
                        pygame.draw.line(screen_6_l2, ORANGE, (150, o2d + 34), (150, o2c + 25), 20)
                        if (my not in range(125,175)):
                            o2c -= 50
                            o2d -= 50
                        else:
                            continue
                    elif (mx in range(o2e,o2f) and my in range(125,175)):
                        pygame.draw.line(screen_6_l2, ORANGE, (o2e - 34, 150), (o2f -25, 150), 20)
                        if (mx not in range(275,325)):
                            o2e += 50
                            o2f += 50
                        else:
                            continue
                    elif (mx in range(275,325) and my in range(o2g,o2h)):
                        pygame.draw.line(screen_6_l2, ORANGE, (300, o2g - 34), (300, o2h - 25), 20)
                        if (my not in range(225,275)):
                            o2g += 50
                            o2h += 50
                        else:
                            continue
                    elif (mx in range(o2i,o2j) and my in range(225,275)):
                        pygame.draw.line(screen_6_l2, ORANGE, (o2j + 34, 250), (o2i + 25, 250), 20)
                        if (done2_o == 0):
                            done2_o = 1
                            flow += 1
                    if (mx in range(o2k,o2l) and my in range(225,275)):
                        pygame.draw.line(screen_6_l2, ORANGE, (o2k -25, 250), (o2l - 16, 250), 20)
                    elif (mx in range(275,325) and my in range(o2m,o2n)):
                        pygame.draw.line(screen_6_l2, ORANGE, (300, o2n + 34), (300, o2m + 25), 20)
                        if (my not in range(125,175)):
                            o2m -= 50
                            o2n -= 50
                        else:
                            continue
                    elif (mx in range(o2o,o2p) and my in range(125,175)):
                        pygame.draw.line(screen_6_l2, ORANGE, (o2p + 34, 150), (o2o + 25, 150), 20)
                        if (mx not in range(125, 175)):
                            o2o -= 50
                            o2p -= 50
                        else:
                            continue
                    elif (mx in range(125,175) and my in range(o2q, o2r)):
                        pygame.draw.line(screen_6_l2, ORANGE, (150, o2q - 34), (150, o2r - 25), 20)
                        if(my not in range(375,425)):
                            o2q += 50
                            o2r += 50
                        else:
                            continue
                    elif (mx in range(o2s,o2t) and my in range(375,425)):
                        pygame.draw.line(screen_6_l2, ORANGE, (o2s - 34, 400), (o2t - 25, 400), 20)
                        if (done2_o == 0):
                            done2_o = 1
                            flow += 1
        if(flow == 4):
            game_over()
            pygame.display.update()
        pygame.display.flip()
