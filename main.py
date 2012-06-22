import os, sys
import pygame
from pygame.locals import *

from helper import *
from gameGlobals import *
from assets import *
import time
import random

def menu():
    selected = False

    total_items = 2
    item_choice = 1
       
    c = 0
    while not selected:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_UP:
                if(item_choice < total_items):
                    item_choice += 1
                else:
                    item_choice = 1


            if event.type == KEYDOWN and event.key == K_DOWN:
                if(item_choice > 1):
                    item_choice -= 1
                else:
                    item_choice = total_items
            if event.type == USEREVENT+2:
                c+=1

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                selected = True

            if event.type == KEYDOWN and event.key == K_RETURN:
                if item_choice == 1:
                    mainGameLoop()
                if item_choice == 2:
                    selected = True
                    
        
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(space, (0,0))
        screen.blit(gases, (0,300))
        screen.blit(planet, (0,0))
        screen.blit(gases2, (0,100))

        menu_choice(item_choice)
        fon = pygame.font.SysFont("",32)
        if c >= len(omega):
            c=0
        screen.blit(omega[c],(0,0))
    
        pygame.display.flip()


def menu_choice(itemNum):
    if itemNum == 1:
        start_text = fon.render("START", 3, (0,255,0))
        screen.blit(trans_bg, (300,300))
        screen.blit(start_text, (400,300))

        end_text = fon.render("END", 3, (255,0,0))
        screen.blit(trans_bg, (300,350))
        screen.blit(end_text, (400,350))
    elif itemNum == 2:
        start_text = fon.render("START", 3, (255,0,0))
        screen.blit(trans_bg, (300,300))
        screen.blit(start_text, (400,300))

        end_text = fon.render("END", 3, (0,255,0))
        screen.blit(trans_bg, (300,350))
        screen.blit(end_text, (400,350))
    



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


            if event.type == KEYDOWN and event.key == K_UP:
                player1.up = True


            if event.type == KEYDOWN and event.key == K_DOWN:
                player1.down = True

            if event.type == KEYDOWN and event.key == K_LEFT:
                player1.left = True

            if event.type == KEYDOWN and event.key == K_RIGHT:
                player1.right = True



            if event.type == KEYUP and event.key == K_UP:
                player1.up = False

            if event.type == KEYUP and event.key == K_DOWN:
                player1.down = False

            if event.type == KEYUP and event.key == K_LEFT:
                player1.left = False

            if event.type == KEYUP and event.key == K_RIGHT:
                player1.right = False

            ############################################################
            #    shooting                                              #
            ############################################################
            if event.type == KEYDOWN and event.key == K_a:
                player1.shoot = True
            if event.type == KEYUP and event.key == K_a:
                player1.shoot = False



            ############################################################
            #    Other logic                                           #
            ############################################################

            if event.type == USEREVENT+1:
                enemies.add(enemy((random.randint(0,WINX),0)))




        allsprites.update()
        player1.particles.update()
        player1.bullets.update()

        screen.blit(background, (0, 0))

        for e in enemies:
            e.update()
            e.bullets.update()
            e.particles.update()
            e.particles.draw(screen)
            e.bullets.draw(screen)
            if e.rect.centerx > WINX or e.rect.centery > WINY or e.rect.centerx < 0 or e.rect.centery < 0:
                e.kill()

        collisions = None
        collisions = pygame.sprite.spritecollide(player1, enemies, True)
        if len(collisions) > 0:
            end = False

        collisions = None
        collisions = pygame.sprite.groupcollide(player1.bullets, enemies, True, True)
        if len(collisions) > 0:
            SCORE += len(collisions)

        fonsurf = fon.render("SCORE: "+str(SCORE),3, (255,0,0))

        screen.blit(fonsurf, (WINX-100,13))
        enemies.draw(screen)
        player1.particles.draw(screen)
        player1.bullets.draw(screen)
        allsprites.draw(screen)
        renderSpace()
        
        #for b in player1.bullets:
        #    b.blitParticles(screen)
        pygame.display.flip()

points = []
def renderSpace():
    if len(points) == 0:
        global points
        for i in range(random.randint(0,800)):
            x= random.randint(0,800)
            y=random.randint(0,600)
            points.append([x,y])
#            points.append((x+1,y+1))

    else:
        moveSpace()
        for p in points:
            pygame.draw.line(screen,(255,0,0),p,p)
#        pygame.draw.lines(screen,(255,0,0),False,points)

def moveSpace():
    global points
    for p in points:
        if p[0] > 800:
            p[0] = p[0]-800
        else:
            p[0] += 1
        if p[1] > 600:
            p[1] = p[1]-600
        else:
            p[1] += 1

###############
#   GLOBALS   #
###############

pygame.init()
pygame.font.init()

fon = pygame.font.SysFont("SpaceYo",16)

screen = pygame.display.set_mode((WINX, WINY))
pygame.display.set_caption('spaceYo')
pygame.mouse.set_visible(0)


omega=[load_no_rect("omega_weapon1.png"), load_no_rect("omega_weapon2.png"),load_no_rect("omega_weapon3.png"),load_no_rect("omega_weapon4.png"),load_no_rect("omega_weapon5.png"),load_no_rect("omega_weapon6.png"),load_no_rect("omega_weapon7.png"),load_no_rect("omega_weapon8.png")]

gases = load_no_rect("star_gases.png")
gases2 = load_no_rect("star_gases_backup.png")
space = load_no_rect("space2.jpg")
planet = load_no_rect("planet.png")

trans_bg = load_no_rect("score_hud.png")
bomb = load_no_rect("bomb.png")



pygame.time.set_timer(USEREVENT+2, 100)



background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))


screen.blit(background, (0, 0))
pygame.display.flip()

player1 = ship()
enemy1 = enemy((300,0))
enemies = pygame.sprite.RenderPlain((enemy1))

allsprites = pygame.sprite.RenderPlain((player1))
#player_group = pygame.sprite.Group(player1)



clock = pygame.time.Clock()

pygame.time.set_timer(USEREVENT+1, 1000)


end = False



menu()


    
        
            
