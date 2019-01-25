import pygame
import sys
import time
import os
from game_over import *
pygame.init()
pygame.display.set_caption("Flow Free -->>")
X = 500
Y = 500
RED = (255,0,0)
GREEN = (50,205,50)
BLUE = (0,0,205)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
#global variables
circ = 0
r5a = 325
r5b = 375
r5c = 175
r5d = 225
r5e = 275
r5f = 325
r5g = 275
r5h = 325
r5i = 275
r5j = 325
r5k = 275
r5l = 325
g5a = 225
g5b = 275
g5c = 225
g5d = 275
g5e = 325
g5f = 375
g5g = 275
g5h = 325
g5i = 225
g5j = 275
g5k = 225
g5l = 275
b5a = 275
b5b = 325
b5c = 175
b5d = 225
b5e = 175
b5f = 225
b5g = 125
b5h = 175
b5i = 175
b5j = 225
b5k = 175
b5l = 225
y5a = 225
y5b = 275
y5c = 225
y5d = 275
y5e = 175
y5f = 225
y5g = 175
y5h = 225
flow = 0
done5_r = 0
done5_g = 0
done5_b = 0
done5_y = 0
barheight = 100                         #It is the total width of the bar
LEFT = 1                                 #for conditions
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

def game_screen_l2():
    global circ
    global r5a
    global r5b
    global r5c
    global r5d
    global r5e
    global r5f
    global r5g
    global r5h
    global r5i
    global r5j
    global r5k
    global r5l
    global g5a
    global g5b
    global g5c
    global g5d
    global g5e
    global g5f
    global g5g
    global g5h
    global g5i
    global g5j
    global g5k
    global g5l
    global b5a
    global b5b
    global b5c
    global b5d
    global b5e
    global b5f
    global b5g
    global b5h
    global b5i
    global b5j
    global b5k
    global b5l
    global y5a
    global y5b
    global y5c
    global y5d
    global y5e
    global y5f
    global y5g
    global y5h
    global flow
    global done5_r
    global done5_g
    global done5_b
    global done5_y
    screen = pygame.display.set_mode((X,Y))
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
                elif(event.type == pygame.K_b):
                    flow = 0
                    return
                    pygame.display.update()
   #Iteration for horizontal lines
        y = 125                                                 #starting point
        while(y <= 375):
            pygame.draw.line(screen , (255 , 153 , 153) , (125 , y) , (375,y))   #code for line from one co-ordinate to another
            y += 50                             #increasing 40 for each iteration because the width of each is 40
        x = 125                                 #Variable for vertical lines
    #Iteration for vertical lines
        while(x <= 375):
            pygame.draw.line(screen , (255,153,153) , (x,125) , (x , 375))
            x += 50
    #Drawing coloured circles
        pygame.draw.circle(screen, RED, (300, 150), 20)
        pygame.draw.circle(screen, GREEN, (300, 200), 20)
        pygame.draw.circle(screen, BLUE, (250, 200), 20)
        pygame.draw.circle(screen, GREEN, (200, 350), 20)
        pygame.draw.circle(screen, YELLOW, (250, 250), 20)
        pygame.draw.circle(screen, YELLOW, (200, 200), 20)
        pygame.draw.circle(screen, BLUE, (150, 350), 20)
        pygame.draw.circle(screen, RED, (250, 350), 20)
    #Vertical Borders
        x = 0
        while(x < bgheight):
            pygame.draw.line(screen , borcolor[x] , ((40 - x),0) , ((40 - x) , Y))
            x += 1
        x = 0
        while(x <  bgheight):
            pygame.draw.line(screen , borcolor[x] , ((X - 40) + x , 0) , ((X - 40) + x , Y))
            x += 1

    #Horizontal Borders
        y = 0
        while(y < bgheight):
            pygame.draw.line(screen , borcolor[y] , (30, (40 - y)) , (X - 30 ,(40 - y)))
            y += 1
        y = 0
        while(y < bgheight):
            pygame.draw.line(screen , borcolor[y] , (30 , (Y-40) + y) , (X - 30,(Y - 40) + y))
            y += 1

        label = font.render("Flows :" , 0 , (255,255,255))
        screen.blit(label,(120,110))
        label1 = font.render("Level - 2" , 0 ,(255,255,255))
        screen.blit(label1,(300,110))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                    pygame.quit()
            if e.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                mx , my = pygame.mouse.get_pos()
                if ((mx in range(280,320) and my in range(130,170)) or (mx in range(230,270) and my in range(330,370))):
                    circ = 1 #RED
                elif ((mx in range(280,320) and my in range(180,220)) or (mx in range(180,220) and my in range(330,370))):
                    circ = 2 #GREEN
                elif ((mx in range(230,270) and my in range(180,220)) or (mx in range(130,170) and my in range(330,370))):
                    circ = 3 #BLUE
                elif ((mx in range(180,220) and my in range(180,220)) or (mx in range(230,270) and my in range(230,270))):
                    circ = 4 #YELLOW
                if (circ == 1):
                    if (mx in range(r5a,r5b) and my in range(125,175)):
                        pygame.draw.line(screen, RED, (r5a - 25, 150), (r5b - 16, 150), 20)
                    elif (mx in range(325,375) and my in range(r5c,r5d)):
                        pygame.draw.line(screen, RED, (350, r5c - 25), (350, r5d - 25), 20)
                        if (my not in range(325,375)):
                            r5c += 50
                            r5d += 50
                        else:
                            continue
                    elif (mx in range(r5e,r5f) and my in range(325,375)):
                        pygame.draw.line(screen, RED, (r5f + 34, 350), (r5e + 25, 350), 20)
                        if(mx not in range(225,275)):
                            r5e -= 50
                            r5f -= 50
                        else:
                            if (done5_r == 0):
                                done5_r = 1
                                flow += 1
                            continue
                    if (mx in range(r5g,r5h) and my in range(325,375)):
                        pygame.draw.line(screen, RED, (r5g - 25, 350), (r5h - 16, 350), 20)
                        if(mx not in range(325,375)):
                            r5g += 50
                            r5h += 50
                        else:
                            continue
                    elif (mx in range(325,375) and my in range(r5i,r5j)):
                        pygame.draw.line(screen, RED, (350, r5j + 34), (350, r5i + 25), 20)
                        if (my not in range(125,175)):
                            r5i -= 50
                            r5j -= 50
                        else:
                            continue
                    elif (mx in range(r5k,r5l) and my in range(125,175)):
                        pygame.draw.line(screen, RED, (r5l + 34, 150), (r5k + 25, 150), 20)
                        if (done5_r == 0):
                            done5_r = 1
                            flow += 1
                elif (circ == 2):
                    if (mx in range(275,325) and my in range(g5a,g5b)):
                        pygame.draw.line(screen, GREEN, (300, g5a - 25), (300, g5b - 25), 20)
                        if (my not in range(275,325)):
                            g5a += 50
                            g5b += 50
                        else:
                            continue
                    elif (mx in range(g5c,g5d) and my in range(275,325)):
                        pygame.draw.line(screen, GREEN, (g5d + 34, 300), (g5c + 25, 300), 20)
                        if(mx not in range(175,225)):
                            g5c -= 50
                            g5d -= 50
                        else:
                            continue
                    elif (mx in range(175,225) and my in range(g5e,g5f)):
                        pygame.draw.line(screen, GREEN, (200, g5e - 34), (200, g5f - 25), 20)
                        if (my not in range(325,375)):
                            g5e += 50
                            g5f += 50
                        else:
                            if (done5_g == 0):
                                done5_g = 1
                                flow += 1
                            continue
                    if (mx in range(175,225) and my in range(g5g,g5h)):
                        pygame.draw.line(screen, GREEN, (200, g5h + 25), (200, g5g + 16), 20)
                        if (my not in range(275, 325)):
                            g5g -= 50
                            g5h -= 50
                        else:
                            continue
                    elif (mx in range(g5i,g5j) and my in range(275,325)):
                        pygame.draw.line(screen, GREEN, (g5i - 34, 300), (g5j - 25, 300), 20)
                        if(mx not in range(275,325)):
                            g5i += 50
                            g5j += 50
                        else:
                            continue
                    elif (mx in range(275,325) and my in range(g5k,g5l)):
                        pygame.draw.line(screen, GREEN, (300, g5l + 34), (300, g5k + 25), 20)
                        if (my not in range(175,225)):
                            g5k -= 50
                            g5l -= 50
                        else:
                            if (done5_g == 0):
                                done5_g = 1
                                flow += 1
                            continue
                elif (circ == 3):
                    if (mx in range(125,175) and my in range(b5a,b5b)):
                        pygame.draw.line(screen, BLUE, (150, b5b + 25), (150, b5a + 25), 20)
                        if (my not in range(125,175)):
                            b5a -= 50
                            b5b -= 50
                        else:
                            continue
                    elif (mx in range(b5c,b5d) and my in range(125,175)):
                        pygame.draw.line(screen, BLUE, (b5c - 34, 150), (b5d - 25, 150), 20)
                        if (mx not in range(225,275)):
                            b5c += 50
                            b5d += 50
                        else:
                            if (done5_b == 0):
                                done5_b = 1
                                flow += 1
                            continue
                    elif (mx in range(225,275) and my in range(b5e,b5f)):
                        pygame.draw.line(screen, BLUE, (250, b5e - 34), (250, b5f - 25), 20)
                    if (mx in range(225,275) and my in range(b5g,b5h)):
                        pygame.draw.line(screen, BLUE, (250, b5h + 25), (250, b5g + 16), 20)
                    elif (mx in range(b5i,b5j) and my in range(125,175)):
                        pygame.draw.line(screen, BLUE, (b5j + 34, 150), (b5i + 25, 150), 20)
                        if (mx not in range(125,175)):
                            b5i -= 50
                            b5j -= 50
                        else:
                            continue
                    elif (mx in range(125,175) and my in range(b5k,b5l)):
                        pygame.draw.line(screen, BLUE, (150, b5k - 34), (150, b5l - 25), 20)
                        if (my not in range(325,375)):
                            b5k += 50
                            b5l += 50
                        else:
                            if (done5_b == 0):
                                done5_b = 1
                                flow += 1
                            continue
                elif (circ == 4):
                    if (mx in range(175,225) and my in range(y5a,y5b)):
                        pygame.draw.line(screen, YELLOW, (200, y5a - 25), (200, y5b - 25), 20)
                    elif (mx in range(y5c,y5d) and my in range(225,275)):
                        pygame.draw.line(screen, YELLOW, (y5c - 34, 250), (y5d - 25, 250), 20)
                        if (done5_y == 0):
                            done5_y = 1
                            flow += 1
                    if (mx in range(y5e,y5f) and my in range(225,275)):
                        pygame.draw.line(screen, YELLOW, (y5f + 16, 250), (y5e + 25, 250), 20)
                    elif (mx in range(175,225) and my in range(y5g,y5h)):
                        pygame.draw.line(screen, YELLOW, (200, y5h + 34), (200, y5g + 25), 20)
                        if (done5_y == 0):
                            done5_y = 1
                            flow += 1
        if(flow == 4):
            game_over()
            pygame.display.update()
        pygame.display.flip()
