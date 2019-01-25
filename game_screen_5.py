import pygame
import sys
import time
import os

pygame.init()
pygame.display.set_caption("Flow Free -->>")
X = 500
Y = 500
from game_over import *
RED = (255,0,0)
GREEN = (50,205,50)
BLUE = (0,0,205)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
#Global Var
ra = 175
rb = 225
circ = 0
rd = 225
rc = 175
rg = 275
rf  = 325
ga = 175
gb = 225
gc = 175
gd = 225
gf = 225
gg = 275
gh = 225
gi = 275
ba = 225
bb = 275
bc = 275
bd = 325
ya = 275
yb = 325
yc = 175
yd = 225
yf = 225
yg = 275
yh = 325
yi = 375
oa = 225
ob = 275
oc = 275
od = 325
of = 325
og = 375
oh = 275
oi = 325
done_o = 0
done_y = 0
done_b = 0
done_g = 0
done_r = 0
flow = 0

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

def game_screen_5():
    global ra
    global rb
    global circ
    global rc
    global rd
    global rg
    global rf
    global ga
    global gb
    global gc
    global gd
    global gf
    global gg
    global gh
    global gi
    global ba
    global bb
    global bc
    global bd
    global ya
    global yb
    global yc
    global yd
    global yf
    global yg
    global yh
    global yi
    global oa
    global ob
    global oc
    global od
    global of
    global og
    global oh
    global oi
    global flow
    global done_r
    global done_y
    global done_g
    global done_o
    global done_b
    game_screen_5 = pygame.display.set_mode((X,Y))
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
                    pygame.display.flip()
   #Iteration for horizontal lines
        y = 125                                                 #starting point
        while(y <= 375):
            pygame.draw.line(game_screen_5, (255 , 153 , 153) , (125 , y) , (375,y))   #code for line from one co-ordinate to another
            y += 50                             #increasing 40 for each iteration because the width of each is 40

        x = 125                                 #Variable for vertical lines

    #Iteration for vertical lines
        while(x <= 375):
            pygame.draw.line(game_screen_5 , (255,153,153) , (x,125) , (x , 375))
            x += 50

    #Drawing coloured circles
        pygame.draw.circle(game_screen_5, RED, (150, 150), 20)
        pygame.draw.circle(game_screen_5, GREEN, (250, 150), 20)
        pygame.draw.circle(game_screen_5, BLUE, (250, 200), 20)
        pygame.draw.circle(game_screen_5, GREEN, (200, 300), 20)
        pygame.draw.circle(game_screen_5, YELLOW, (300, 300), 20)
        pygame.draw.circle(game_screen_5, YELLOW, (350, 150), 20)
        pygame.draw.circle(game_screen_5, BLUE, (250, 350), 20)
        pygame.draw.circle(game_screen_5, RED, (200, 350), 20)
        pygame.draw.circle(game_screen_5, ORANGE, (350, 200), 20)
        pygame.draw.circle(game_screen_5, ORANGE, (300, 350), 20)



    #Vertical Borders
        x = 0
        while(x < bgheight):
            pygame.draw.line(game_screen_5 , borcolor[x] , ((40 - x),0) , ((40 - x) , Y))
            x += 1
        x = 0
        while(x <  bgheight):
            pygame.draw.line(game_screen_5 , borcolor[x] , ((X - 40) + x , 0) , ((X - 40) + x , Y))
            x += 1

    #Horizontal Borders
        y = 0
        while(y < bgheight):
            pygame.draw.line(game_screen_5 , borcolor[y] , (30, (40 - y)) , (X - 30 ,(40 - y)))
            y += 1
        y = 0
        while(y < bgheight):
            pygame.draw.line(game_screen_5, borcolor[y] , (30 , (Y-40) + y) , (X - 30,(Y - 40) + y))
            y += 1

        label = font.render("Flows :"+str(flow) , 0 , (255,255,255))
        game_screen_5.blit(label,(120,110))
        label1 = font.render("Level - 1" , 0 ,(255,255,255))
        game_screen_5.blit(label1,(300,110))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                    pygame.quit()
            if e.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                mx , my = pygame.mouse.get_pos()
                # Deciding colour based on mouse position
                if((mx in range(130,170) and my in range(130,170)) or (mx in range(180,220) and my in range(330,370))):
                       circ = 1 #RED
                elif ((mx in range(230,270) and my in range(130,170)) or (mx in range(180,220) and my in range(280,320))):
                        circ = 2 #GREEN
                elif ((mx in range(230,270) and my in range(180,220)) or (mx in range(230,270) and my in range(330,370))):
                        circ = 3 #BLUE
                elif ((mx in range(330,370) and my in range(130,170)) or (mx in range(280,320) and my in range(280,320))):
                        circ = 4 #YELLOW
                elif ((mx in range(330,370) and my in range(180,220)) or (mx in range(280,320) and my in range(330,370))):
                        circ = 5 #ORANGE

                # If the colour is RED
                if(circ == 1):
                    if(mx in range(125,175) and my in range(ra , rb) and my not in range(325,350)):
                        pygame.draw.line(game_screen_5,RED ,(150,ra-25) , (150,rb-25),20)
                        if (my not in range(325,375)):
                            ra += 50
                            rb += 50
                        else:
                            continue
                    elif(mx in range(rc,rd) and my in range(325,375)):
                        pygame.draw.line(game_screen_5,RED,(rc-34,350) , (rd-25,350),20)
                        if(done_r == 0):
                            done_r = 1
                            flow +=1
                    if(mx in range(rc,rd) and my in range(325,375)):
                        pygame.draw.line(game_screen_5,RED,(rd-25,350) , (rc-34,350),20)
                    elif(mx in range(125,175) and my in range(rg , rf)):
                        pygame.draw.line(game_screen_5,RED ,(150,rf+25) , (150,rg+25),20)
                        if (my not in range(125,175)):
                            rg -= 50
                            rf -= 50
                        else:
                            if(done_r == 0):
                                done_r = 1
                                flow += 1
                            continue
                #GREEN
                elif (circ == 2):
                    if (mx in range(ga,gb) and my in range(125,175)):
                        pygame.draw.line(game_screen_5, GREEN, (gb + 25,150), (ga + 16,150),20)
                    elif (mx in range(175,225) and my in range(gc,gd)):
                        pygame.draw.line(game_screen_5, GREEN, (200, gc-34), (200, gd-25),20)
                        if (my not in range(275,325)):
                            gc += 50
                            gd += 50
                        else:
                            if(done_g == 0):
                                done_g = 1
                                flow += 1
                            continue
                    if (mx in range(175,225) and my in range(gf,gg)):
                        pygame.draw.line(game_screen_5, GREEN, (200, gg+25), (200, gf+25),20)
                        if(my not in range(125,175)):
                            gf -= 50
                            gg -= 50
                        else:
                            continue

                    elif(mx in range(gh,gi) and my in range(125,175)):
                        pygame.draw.line(game_screen_5, GREEN, (gh-34, 150), (gi-25, 150),20)
                        if(done_g == 0):
                            done_g = 1
                            flow += 1

                #BLUE
                elif (circ == 3):
                    if mx in range(225,275) and my in range(ba,bb):
                        pygame.draw.line(game_screen_5, BLUE, (250, ba-25), (250, bb - 25), 20)
                        if (my not in range(325,375)):
                            ba += 50
                            bb += 50
                        else:
                            if(done_b == 0):
                                done_b = 1
                                flow += 1
                            continue
                    if mx in range(225,275) and my in range(bc, bd):
                        pygame.draw.line(game_screen_5, BLUE, (250, bd+25), (250, bc + 25), 20)
                        if (my not in range(175,225)):
                            bc -= 50
                            bd -= 50
                        else:
                            if(done_b == 0):
                                done_b = 1
                                flow += 1
                            continue
                #YELLOW
                elif (circ == 4):
                    if (mx in range(ya,yb) and my in range(125,175)):
                        pygame.draw.line(game_screen_5, YELLOW, (yb + 25,150), (ya + 16,150),20)
                    elif (mx in range(275,325) and my in range(yc,yd)):
                        pygame.draw.line(game_screen_5, YELLOW, (300, yc-34), (300, yd-25),20)
                        if (my not in range(275,325)):
                            yc += 50
                            yd += 50
                        else:
                            if(done_y == 0):
                                done_y = 1
                                flow += 1
                            continue

                    if (mx in range(275,325) and my in range(yf,yg)):
                        pygame.draw.line(game_screen_5, YELLOW, (300, yg+25), (300, yf+25),20)
                        if (my not in range(125,175)):
                            yf -= 50
                            yg -= 50
                        else:
                            continue

                    elif (mx in range(yh,yi) and my in range(125,175)):
                        pygame.draw.line(game_screen_5, YELLOW, (yh - 34,150), (yi - 25,150),20)
                        if(done_y == 0):
                                done_y = 1
                                flow += 1

                #ORANGE
                elif (circ == 5):
                    if (mx in range(325,375) and my in range(oa,ob)):
                        pygame.draw.line(game_screen_5, ORANGE, (350, oa-25), (350, ob-25),20)
                        if (my not in range(325,375)):
                            oa += 50
                            ob += 50
                        else:
                            continue
                    elif (mx in range(oc,od) and my in range(325,375)):
                        pygame.draw.line(game_screen_5, ORANGE, (od + 34, 350), (oc + 25, 350),20)
                        if(done_o == 0):
                            done_o = 1
                            flow += 1

                    if (mx in range(of,og) and my in range (325,375)):
                        pygame.draw.line(game_screen_5, ORANGE, (og-25, 350), (of-16, 350),20)
                    elif (mx in range(325,375) and my in range(oh,oi)):
                        pygame.draw.line(game_screen_5, ORANGE, (350, oi+34), (350, oh+25),20)
                        if (my  not in range(175,225)):
                            oh -= 50
                            oi -= 50
                        else:
                            if(done_o == 0):
                                done_o = 1
                                flow += 1
                            continue
        if(flow == 5):
            game_over()
            pygame.display.update()
            print str(flow)
        pygame.display.flip()
