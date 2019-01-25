import pygame
import sys
import time
import os
from game_over import *
pygame.init()
pygame.display.set_caption("Flow Free -->>")
X = 550
Y = 550

RED = (255,0,0)
GREEN = (50,205,50)
BLUE = (0,0,205)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
#global variables
circ = 0
r6a = 125
r6b = 175
r6c = 125
r6d = 175
r6f = 175
r6g = 225
r6h = 175
r6j = 225
r6k = 275
r6l = 325
r6m = 275
r6n = 325
r6o = 225
r6p = 275
r6q = 225
r6r = 275
r6s = 175
r6t = 225
r6u = 175
r6v = 225
r6w = 175
r6x = 225
r6y = 175
r6z = 225
b6a = 175
b6b = 225
b6c = 275
b6d = 325
b6e = 225
b6f = 275
b6g = 175
b6h = 225
b6i = 225
b6j = 275
b6k = 125
b6l = 175
g6a = 325
g6b = 375
g6c = 175
g6d = 225
g6e = 275
g6f = 325
g6g = 225
g6h = 275
g6i = 275
g6j = 325
g6k = 275
g6l = 325
y6a = 175
y6b = 225
y6c = 325
y6d = 375
y6e = 325
y6f = 375
y6g = 175
y6h = 225
y6i = 125
y6j = 175
y6k = 325
y6l = 375
y6m = 175
y6n = 225
y6o = 325
y6p = 375
flow = 0
done6_r = 0
done6_b = 0
done6_g = 0
done6_y = 0
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
def game_screen_6():
    global circ
    global r6a
    global r6b
    global r6c
    global r6d
    global r6f
    global r6g
    global r6h
    global r6j
    global r6k
    global r6l
    global r6m
    global r6n
    global r6o
    global r6p
    global r6q
    global r6r
    global r6s
    global r6t
    global r6u
    global r6v
    global r6w
    global r6x
    global r6y
    global r6z
    global b6a
    global b6b
    global b6c
    global b6d
    global b6e
    global b6f
    global b6g
    global b6h
    global b6i
    global b6j
    global b6k
    global b6l
    global g6a
    global g6b
    global g6c
    global g6d
    global g6e
    global g6f
    global g6g
    global g6h
    global g6i
    global g6j
    global g6k
    global g6l
    global y6a
    global y6b
    global y6c
    global y6d
    global y6e
    global y6f
    global y6g
    global y6h
    global y6i
    global y6j
    global y6k
    global y6l
    global y6m
    global y6n
    global y6o
    global y6p
    global flow
    global done6_r
    global done6_b
    global done6_g
    global done6_y
    screen_6 = pygame.display.set_mode((X,Y))
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
            pygame.draw.line(screen_6 , (255 , 153 , 153) , (125 , y) , (425,y))   #code for line from one co-ordinate to another
            y += 50                             #increasing 40 for each iteration because the width of each is 40
        x = 125                                   #Variable for vertical lines
    #Iteration for vertical lines
        while(x <= 425):
            pygame.draw.line(screen_6 , (255,153,153) , (x,125) , (x , 425))
            x += 50
    #Drawing coloured circles
        pygame.draw.circle(screen_6, RED, (200, 200), 20)
        pygame.draw.circle(screen_6, GREEN, (350, 200), 20)
        pygame.draw.circle(screen_6, BLUE, (150, 250), 20)
        pygame.draw.circle(screen_6, GREEN, (150, 300), 20)
        pygame.draw.circle(screen_6, YELLOW, (150, 400), 20)
        pygame.draw.circle(screen_6, YELLOW, (300, 200), 20)
        pygame.draw.circle(screen_6, BLUE, (250, 300), 20)
        pygame.draw.circle(screen_6, RED, (300, 300), 20)
    #Vertical Borders
        x = 0
        while(x < bgheight):
            pygame.draw.line(screen_6 , borcolor[x] , ((40 - x),0) , ((40 - x) , Y))
            x += 1
        x = 0
        while(x <  bgheight):
            pygame.draw.line(screen_6 , borcolor[x] , ((X - 40) + x , 0) , ((X - 40) + x , Y))
            x += 1
    #Horizontal Borders
        y = 0
        while(y < bgheight):
            pygame.draw.line(screen_6 , borcolor[y] , (30, (40 - y)) , (X - 30 ,(40 - y)))
            y += 1
        y = 0
        while(y < bgheight):
            pygame.draw.line(screen_6 , borcolor[y] , (30 , (Y-40) + y) , (X - 30,(Y - 40) + y))
            y += 1
        label = font.render("Flows :" , 0 , (255,255,255))
        screen_6.blit(label,(130,110))
        label1 = font.render("Level - 1" , 0 ,(255,255,255))
        screen_6.blit(label1,(200,110))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                    pygame.quit()
            if e.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                mx , my = pygame.mouse.get_pos()
                #deciding colour based on mouse position
                if((mx in range(180,220) and my in range(180,220)) or (mx in range(280,320) and my in range(280,320))):
                    circ = 1 #RED
                elif((mx in range(130,170) and my in range(230,270)) or (mx in range(230,270) and my in range(280,320))):
                    circ = 2 #BLUE
                elif((mx in range(130,170) and my in range(280,320)) or (mx in range(330,370) and my in range(180,220))):
                    circ = 3 #GREEN
                elif((mx in range(130,170) and my in range(380,420)) or (mx in range(280,320) and my in range(180,220))):
                    circ = 4 #YELLOW

                #RED
                if (circ == 1):
                    if (mx in range(r6a,r6b) and my in range(175,225)):
                        pygame.draw.line(screen_6, RED, (r6b + 25, 200), (r6a +16, 200), 20)
                    elif (mx in range(125,175) and my in range(r6c,r6d)):
                        pygame.draw.line(screen_6, RED, (150, r6d + 25), (150, r6c +16), 20)
                    elif (mx in range(r6f,r6g) and my in range(125,175)):
                        pygame.draw.line(screen_6, RED, (r6f -25, 150), (r6g - 25, 150), 20)
                        if (mx not in range(225,275)):
                            r6f += 50
                            r6g += 50
                        else:
                            continue
                    elif (mx in range(225,275) and my in range(r6h,r6j)):
                        pygame.draw.line(screen_6, RED, (250, r6h - 34), (250, r6j - 25), 20)
                        if (my not in range(225,275)):
                            r6h += 50
                            r6j += 50
                        else:
                            continue
                    elif (mx in range(r6k,r6l) and my in range(225,275)):
                        pygame.draw.line(screen_6, RED, (r6k - 34, 250), (r6l - 25, 250), 20)

                    #r6m = 275
                    #r6n = 325
                    elif (mx in range(275,325) and my in range(r6m,r6n)):
                        pygame.draw.line(screen_6, RED, (300, r6m - 34), (300, r6n - 25), 20)
                        if (done6_r == 0):
                            done6_r = 1
                            flow += 1
                    if (mx in range(275,325) and my in range(r6o, r6p)):
                        pygame.draw.line(screen_6, RED, (300, r6p + 25), (300, r6o + 16), 20)
                    elif (mx in range(r6q,r6r) and my in range(225, 275)):
                        pygame.draw.line(screen_6, RED, (r6r + 25, 250), (r6q + 25, 250), 20)
                    elif (mx in range(225,275) and my in range(r6s, r6t)):
                        pygame.draw.line(screen_6, RED, (250,r6t + 34), (250,r6s + 25), 20)
                        if (my not in range(125,175)):
                            r6s -= 50
                            r6t -= 50
                        else:
                            continue
                    elif (mx in range(r6u,r6v) and my in range(125, 175)):
                        pygame.draw.line(screen_6, RED, (r6v + 34, 150), (r6u + 25, 150), 20)
                        if (mx not in range(125,175)):
                            r6u -= 50
                            r6v -= 50
                        else:
                            continue
                    elif (mx in range(125,175) and my in range(r6w, r6x)):
                        pygame.draw.line(screen_6, RED, (150, r6w - 25), (150, r6x - 25), 20)
                    elif (mx in range(r6y,r6z) and my in range(175, 225)):
                        pygame.draw.line(screen_6, RED, (r6y - 34, 200), (r6z - 25, 200), 20)
                        if (done6_r == 0):
                            done6_r = 1
                            flow += 1
                elif (circ == 2):
                    if (mx in range(b6a, b6b) and my in range(225,275)):
                        pygame.draw.line(screen_6, BLUE, (b6a - 25, 250), (b6b - 25, 250), 20)
                    elif (mx in range(175,225) and my in range(b6c,b6d)):
                        pygame.draw.line(screen_6, BLUE, (200, b6c - 34), (200, b6d - 25), 20)
                    elif (mx in range(b6e,b6f) and my in range(275,325)):
                        pygame.draw.line(screen_6, BLUE, (b6e - 34, 300), (b6f - 25, 300), 20)
                        if (done6_b == 0):
                            done6_b = 1
                            flow += 1
                    if (mx in range(b6g,b6h) and my in range(275,325)):
                        pygame.draw.line(screen_6, BLUE, (b6h + 25, 300), (b6g + 16, 300), 20)
                    elif (mx in range(175,225) and my in range(b6i, b6j)):
                        pygame.draw.line(screen_6, BLUE, (200, b6j + 25), (200, b6i + 16), 20)
                    elif (mx in range(b6k,b6l) and my in range(225,275)):
                        pygame.draw.line(screen_6, BLUE, (b6l + 25, 250), (b6k + 25, 250), 20)
                        if (done6_b == 0):
                            done6_b = 1
                            flow += 1
                elif(circ == 3):
                    if(mx in range(125,175) and my in range(g6a,g6b)):
                        pygame.draw.line(screen_6, GREEN, (150, g6a - 25), (150, g6b - 16), 20)
                    elif(mx in range(g6c,g6d) and my in range(325,375)):
                        pygame.draw.line(screen_6, GREEN, (g6c - 25, 350), (g6d - 16, 350), 20)
                        if (mx not in range(325,375)):
                            g6c += 50
                            g6d += 50
                        else:
                            continue
                    elif(mx in range(325,375) and my in range(g6e,g6f)):
                        pygame.draw.line(screen_6, GREEN, (350, g6f + 25), (350, g6e + 25), 20)
                        if (my not in range(175,225)):
                            g6e -= 50
                            g6f -= 50
                        else:
                            if (done6_g == 0):
                                done6_g = 1
                                flow += 1
                            continue
                    if(mx in range(325, 375) and my in range(g6g,g6h)):
                        pygame.draw.line(screen_6, GREEN, (350, g6g - 25), (350, g6h - 25), 20)
                        if (my not in range(325,375)):
                            g6g += 50
                            g6h += 50
                        else:
                            continue
                    elif (mx in range(g6i,g6j) and my in range(325,375)):
                        pygame.draw.line(screen_6, GREEN, (g6j + 34, 350), (g6i + 25, 350), 20)
                        if (mx not in range(125,175)):
                            g6i -= 50
                            g6j -= 50
                        else:
                            continue
                    elif (mx in range(125,175) and my in range(g6k,g6l)):
                        pygame.draw.line(screen_6, GREEN, (150, g6l + 34), (150, g6k + 25), 20)
                        if (done6_g == 0):
                            done6_g = 1
                            flow += 1
                elif(circ == 4):
                    if(mx in range(y6a,y6b) and my in range(375, 425)):
                        pygame.draw.line(screen_6, YELLOW, (y6a - 25, 400), (y6b - 25, 400), 20)
                        if (mx not in range(375,425)):
                            y6a += 50
                            y6b += 50
                        else:
                            continue
                    elif (mx in range(375,425) and my in range(y6c,y6d)):
                        pygame.draw.line(screen_6, YELLOW, (400, y6d + 34), (400, y6c + 25), 20)
                        if (my not in range(125,175)):
                            y6c -= 50
                            y6d -= 50
                        else:
                            continue
                    elif (mx in range(y6e,y6f) and my in range(125,175)):
                        pygame.draw.line(screen_6, YELLOW, (y6f + 34, 150), (y6e + 25, 150), 20)
                        if (mx not in range(275,325)):
                            y6e -= 50
                            y6f -= 50
                        else:
                            continue
                    elif (mx in range(275,325) and my in range(y6g,y6h)):
                        pygame.draw.line(screen_6, YELLOW, (300, y6g - 34), (300, y6h - 25), 20)
                        if (done6_y == 0):
                            done6_y = 1
                            flow += 1
                    if (mx in range(275,325) and my in range(y6i,y6j)):
                        pygame.draw.line(screen_6, YELLOW, (300, y6j + 25), (300, y6i + 16), 20)
                    elif (mx in range(y6k,y6l) and my in range(125,175)):
                        pygame.draw.line(screen_6, YELLOW, (y6k - 25, 150), (y6l - 16, 150), 20)
                        if (mx not in range(375,425)):
                            y6k += 50
                            y6l += 50
                        else:
                            continue
                    elif (mx in range(375,425) and my in range(y6m,y6n)):
                        pygame.draw.line(screen_6, YELLOW, (400, y6m - 25), (400, y6n - 25), 20)
                        if (my not in range(375,425)):
                            y6m += 50
                            y6n += 50
                        else:
                            continue
                    elif (mx in range(y6o,y6p) and my in range(375,425)):
                        pygame.draw.line(screen_6, YELLOW, (y6p + 34, 400), (y6o + 25, 400), 20)
                        if (mx not in range(125,175)):
                            y6o -= 50
                            y6p -= 50
                        else:
                            if (done6_y == 0):
                                done6_y = 1
                                flow += 1
                            continue
        if(flow == 4):
            game_over()
            pygame.display.update()
        pygame.display.flip()
