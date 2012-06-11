import os, sys
import pygame
from pygame.locals import *
import time
import random
import math

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



def render1():
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
