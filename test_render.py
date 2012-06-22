import os, sys
import pygame
from pygame.locals import *
import time
import random
import math


def point(p, c, surf):
    pygame.draw.line(surf,c,p,p)



end = False
def draw_sin():
    w = 2
    l = []
    for i in range(361):
        x = w*i+1
        y = (math.sin(i)*100)+100
        p = (x,y)
        
        l.append(p)

    print l
#    pygame.draw.lines(screen, (255,0,0),True,[(1,1),(1,100),(100,1)])
    pygame.draw.lines(screen, (255,0,0),True,l)



class star:
    def __init__(self):
        pass

stars = []


def gen_space():
    global stars
    for i in range(1000):
        stars.append([random.randint(0,WINX),random.randint(0,WINY)])
        

def drawPoints(points, c, surf):
    for p in points:
        point(p,c,surf)

def rotatePoints(points):
    for p in points:
        y = p[1]
        x = p[0]
        p[0] = y
        p[1] = x

    return points

def render_circle_animation(points, index):
    pygame.draw.circle(screen,(255,0,255),points[index],32)

def render1():
    global stars
    speed = 1
    for s in stars:
        if s[1] > WINY:
            s[1] = 0
            s[0] = random.randint(0,WINX)
        else:
            s[1] += speed

        pygame.draw.line(screen,(255,random.randint(0,255),0),s,s)


# http://escience.anu.edu.au/lecture/cg/Circle/symmetry4.en.html <-- is the algorithm I used.
def circle(xCenter, yCenter, radius, c):
    x = 1
    r2 = radius*radius
    for x in range(radius):
        y = int(math.sqrt(r2 - x*x) + 0.5)
        pygame.draw.line(screen,c, (xCenter + x,yCenter + y),(xCenter + x, yCenter + y))
        pygame.draw.line(screen,c, (xCenter + x,yCenter - y),(xCenter + x, yCenter - y))
        pygame.draw.line(screen,c, (xCenter - x,yCenter + y),(xCenter - x, yCenter + y))
        pygame.draw.line(screen,c, (xCenter - x,yCenter - y),(xCenter - x, yCenter - y))
    
def circle_type2(xCenter, yCenter, radius, c):
    x = 1
    r2 = radius*radius
    while(x < radius):
        y = int(math.sqrt(r2 - x*x) + 0.5)
        pygame.draw.line(screen,c, (xCenter + x,yCenter + y),(xCenter + x, yCenter + y))
        pygame.draw.line(screen,c, (xCenter + x,yCenter - y),(xCenter + x, yCenter - y))
        pygame.draw.line(screen,c, (xCenter - x,yCenter + y),(xCenter - x, yCenter + y))
        pygame.draw.line(screen,c, (xCenter - x,yCenter - y),(xCenter - x, yCenter - y))
        x = x + 5
        
def circle_type3(xCenter, yCenter, radius, c):
    x = 1
    r2 = radius*radius

    pygame.draw.line(screen,c, (xCenter,yCenter + radius),(xCenter, yCenter + radius))
    pygame.draw.line(screen,c, (xCenter,yCenter + radius),(xCenter, yCenter + radius))
    pygame.draw.line(screen,c, (xCenter + radius, yCenter),(xCenter + radius, yCenter))
    pygame.draw.line(screen,c, (xCenter - radius,yCenter),(xCenter - radius, yCenter))
    
    y = int(math.sqrt(r2 - x*x) + 0.5)    
    while(x < radius):
        y = int(math.sqrt(r2 - x*x) + 0.5)    
        pygame.draw.line(screen,c, (xCenter + x,yCenter + y),(xCenter + x, yCenter + y))
        pygame.draw.line(screen,c, (xCenter + x,yCenter - y),(xCenter + x, yCenter - y))
        pygame.draw.line(screen,c, (xCenter - x,yCenter + y),(xCenter - x, yCenter + y))
        pygame.draw.line(screen,c, (xCenter - x,yCenter - y),(xCenter - x, yCenter - y))
        x = x + 1

def render_circle_points(xCenter, yCenter, radius, rate=1):
    points = []
    x = 1
    r2 = radius*radius
    
    points.append([xCenter,yCenter + radius])
    points.append([xCenter,yCenter - radius])
    points.append([xCenter+radius,yCenter])
    points.append([xCenter-radius,yCenter])
        
    y = int(math.sqrt(r2 - x*x) + 0.5)    
    while(x < radius):
        y = int(math.sqrt(r2 - x*x) + 0.5)
        points.append([xCenter+x, yCenter+y])
        points.append([xCenter+x, yCenter-y])
        points.append([xCenter-x, yCenter+y])
        points.append([xCenter-x, yCenter-y])
        x = x + rate

    return points










        


    
    


def screen_craze():
    # (x-h)^2 + (y-k)^2 = r^2
    # y = r-x-h-k
    # c = (h,k)
    l = []
    r = random.randint(1,3)

    s = pygame.Surface((WINX,WINY))
    if r == 1:
        for i in range(255):
            pygame.draw.line(s,(i,0,0),(0,(i*2)+90),(WINX,(i*2)+90),3)
        r = 2
    elif r == 2:
        for i in range(255):
            pygame.draw.line(s,(0,0,i),(0,(i*2)+90),(WINX,(i*2)+90),3)
        r = 3
    else:
        for i in range(255):
            pygame.draw.line(s,(0,i,0),(0,(i*2)+90),(800,(i*2)+90),3)
        r = 1

#    s = pygame.Surface((100,100))
    screen.blit(s,(0,0))
#    pygame.draw.lines(screen, (255,0,0),True,l)
 
 
    

def mainGameLoop():
    SCORE = 0
    pointz = render_circle_points(400,300,100,2)
    pointz += rotatePoints(pointz)
#    pointz.sort()
    pointz = sorted(pointz, key=lambda point: pointz[0])	
    print pointz
    pointz_flag = True
    index = 0
    while not end:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                global end
                SystemExit
                end = True
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                global end
                end = True
            
            if event.type == MOUSEBUTTONDOWN:
                pass

            if event.type == MOUSEBUTTONUP:
                pass

            ############################################################
            #    Movement                                              #
            ############################################################


#             if event.type == KEYDOWN and event.key == K_UP:
#                 player1.up = True


#             if event.type == KEYDOWN and event.key == K_DOWN:
#                 player1.down = True

#             if event.type == KEYDOWN and event.key == K_LEFT:
#                 player1.left = True

#             if event.type == KEYDOWN and event.key == K_RIGHT:
#                 player1.right = True



#             if event.type == KEYUP and event.key == K_UP:
#                 player1.up = False

#             if event.type == KEYUP and event.key == K_DOWN:
#                 player1.down = False

#             if event.type == KEYUP and event.key == K_LEFT:
#                 player1.left = False

#             if event.type == KEYUP and event.key == K_RIGHT:
#                 player1.right = False

#             ############################################################
#             #    shooting                                              #
#             ############################################################
#             if event.type == KEYDOWN and event.key == K_a:
#                 player1.shoot = True
#             if event.type == KEYUP and event.key == K_a:
#                 player1.shoot = False



#             ############################################################
#             #    Other logic                                           #
#             ############################################################

#             if event.type == USEREVENT+1:
#                 enemies.add(enemy((random.randint(0,WINX),0)))
#             


        screen.blit(background, (0, 0))
	render1()
#        circle_type3(400,300,100,(0,255,0))


#	pointz = rotatePoints(pointz)

	p_rate = 2
	if pointz_flag:
            if index < len(pointz)-p_rate:
                index+=p_rate
            else:
                pointz_flag = False
                
	if pointz_flag == False:
            if index > 0:
                index = index - p_rate
            else:
                pointz_flag = True
                
                
            
        render_circle_animation(pointz,index)
#	drawPoints(pointz,(255,255,0),screen)

        pygame.display.flip()


###############
#   GLOBALS   #
###############
WINX = 800
WINY = 600

pygame.init()
pygame.font.init()

fon = pygame.font.SysFont("SpaceYo",16)

screen = pygame.display.set_mode((WINX, WINY))
pygame.display.set_caption('spaceYo')
pygame.mouse.set_visible(0)

gen_space()

pygame.time.set_timer(USEREVENT+2, 100)



background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))


screen.blit(background, (0, 0))
pygame.display.flip()



clock = pygame.time.Clock()

pygame.time.set_timer(USEREVENT+1, 1000)



end = False

mainGameLoop()
