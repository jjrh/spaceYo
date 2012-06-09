import os, sys
import pygame
from pygame.locals import *
import time
import random





#######################
#  Helper functions   #
#######################

def load_image(name, colorkey=None):
    fullname = os.path.join('visuals', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert_alpha()
    #if colorkey is not None:
    #    if colorkey is -1:
    #        colorkey = image.get_at((0,0))
    #    image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_no_rect(name):
    fullname = os.path.join('visuals', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert_alpha()
    return image



class ship(pygame.sprite.Sprite):
    def __init__(self):
        print "here"
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("ship.png")

        self.image_normal = self.image
        self.image_left, self.rect_left = load_image("ship_left.png")
        self.image_right, self.rect_right = load_image("ship_right.png")
        
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.timer = pygame.time.get_ticks()

        self.rate = 10

        self.particles = pygame.sprite.Group()
        self.max_particles = 30

        self.bullets = pygame.sprite.Group()
        self.bullet_speed = 10
        self.bullet_rate = 1000 # in mili seconds
        self.shoot = False
        self.last_shot = self.timer
        

    def update(self):
        if self.left:
            self.rect = self.rect.move(-self.rate,0)
            self.image = self.image_left
            for i in range(self.max_particles):
                self.particles.add(particle((255,0,0),(-self.rate,0),self.rect.center,self.rect.height/2))
        if self.right:
            self.rect = self.rect.move(self.rate,0)
            self.image = self.image_right
            
            for i in range(self.max_particles):
                self.particles.add(particle((255,0,0),(self.rate,0),self.rect.center,self.rect.height/2))
                
        if self.up:
             self.rect = self.rect.move(0,-self.rate)
             self.image = self.image_normal
             for i in range(self.max_particles):
                 self.particles.add(particle((255,0,0),(0,self.rate),self.rect.center,self.rect.width/2))

             
        if self.down:
             self.rect = self.rect.move(0,self.rate)
             self.image = self.image_normal
             for i in range(self.max_particles):
                 self.particles.add(particle((255,0,0),(0,-self.rate),self.rect.center,self.rect.width/2))

        if self.left == False and self.right == False and self.up == False and self.down == False:
            self.image = self.image_normal

        if self.shoot == True and (pygame.time.get_ticks() - self.last_shot) > self.bullet_rate:
            self.bullets.add(bullet((0,-self.bullet_speed), self.rect.center))
            self.last_shot = pygame.time.get_ticks()
            

        # Check the particles to see if they have left the viewable area on the screen
        # if they have we remove them from the group and kill them.
        for s in self.particles:
            if s.rect.centerx > WINX or s.rect.centery > WINY:
                s.kill()
            elif s.rect.centerx < 0 or s.rect.centery < 0:
                s.kill()
                
        for b in self.bullets:
            if b.rect.centerx > WINX or b.rect.centery > WINY:
                b.kill()
            elif b.rect.centerx < 0 or b.rect.centery < 0:
                b.kill()


    def changeColor(self):
        pyarray = pygame.PixelArray(self.image)
        for x in pyarray:
            for y in x:
                print "||",y
                if y == 1249553:
                    pyarray[x][y] = ((255,0,0))
                if y == 2555904:
                    pyarray[x][y] = ((255,0,0))
                else:
                    pyarray[x][y] = ((255,255,255))

            
        

class particle(pygame.sprite.Sprite):
    def __init__(self, color, force, loc,randomness=10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1,1))
        self.rect = self.image.get_rect()
        self.image.fill(color)
        self.rect.center = loc
        self.randomness = randomness
        self.rect.centerx = self.rect.centerx+random.randint(-self.randomness,self.randomness)
        self.rect.centery = self.rect.centery+random.randint(-self.randomness,self.randomness)
        self.xForce = force[0]
        self.yForce = force[1]
        self.inc = 0.1
    def update(self):
        if(self.xForce > 0):
            self.rect = self.rect.move(self.xForce+random.randint(0,10)+int(self.inc), self.yForce)
        if(self.xForce < 0):
            self.rect = self.rect.move(self.xForce+random.randint(-10,0)-int(self.inc), self.yForce)
        if(self.yForce > 0):
            self.rect = self.rect.move(self.xForce, self.yForce+random.randint(0,10)+int(self.inc))
        if(self.yForce < 0):
            self.rect = self.rect.move(self.xForce, self.yForce+random.randint(-10,0)-int(self.inc))
        self.inc +=0.1


class bullet(pygame.sprite.Sprite):
    def __init__(self, force, loc):
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect = load_image("bullet.png")
        self.rect.center = loc
        self.xForce = force[0]
        self.yForce = force[1]
        self.inc = 0.1
    def update(self):
        if(self.xForce > 0):
            self.rect = self.rect.move(self.xForce+random.randint(0,10)+int(self.inc), self.yForce)
        if(self.xForce < 0):
            self.rect = self.rect.move(self.xForce+random.randint(-10,0)-int(self.inc), self.yForce)
        if(self.yForce > 0):
            self.rect = self.rect.move(self.xForce, self.yForce+random.randint(0,10)+int(self.inc))
        if(self.yForce < 0):
            self.rect = self.rect.move(self.xForce, self.yForce+random.randint(-10,0)-int(self.inc))
        self.inc +=0.1



class enemy(pygame.sprite.Sprite):
    def __init__(self, loc):
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect = load_image("enemyship_5.png")
        self.timer = pygame.time.get_ticks()
        self.rect.topleft = loc
        self.rate = 10
        self.speed = self.rate
        
        self.particles = pygame.sprite.Group()
        self.max_particles = 30

        self.bullets = pygame.sprite.Group()
        self.bullet_speed = 10
        self.bullet_rate = 100 # in mili seconds
        self.shoot = False
        self.last_shot = self.timer

        self.last_direction_change = self.timer
        self.direction = 1
    def update(self):
        self.shooting_ai_2()
        
        for s in self.particles:
            if s.rect.centerx > WINX or s.rect.centery > WINY:
                s.kill()
            elif s.rect.centerx < 0 or s.rect.centery < 0:
                s.kill()
                
        for b in self.bullets:
            if b.rect.centerx > WINX or b.rect.centery > WINY:
                b.kill()
            elif b.rect.centerx < 0 or b.rect.centery < 0:
                b.kill()
    def shooting_ai_1(self):

        if(pygame.time.get_ticks() - self.last_direction_change) > 2000:
            self.direction = self.direction*-1
            self.last_direction_change = pygame.time.get_ticks()
        
        self.rect = self.rect.move(self.direction*self.speed,1)
        if self.rect.centerx > WINX:
            self.direction = -1
        if self.rect.centerx < 0:
            self.direction = 1
        self.shoot_mechanic()

    def shooting_ai_2(self):
        self.rect = self.rect.move(0,self.speed)

        # Check the particles to see if they have left the viewable area on the screen
        # if they have we remove them from the group and kill them.
    def shoot_mechanic(self):
        if (pygame.time.get_ticks() - self.last_shot) > self.bullet_rate:
            self.bullets.add(bullet((0,self.bullet_speed), self.rect.center))
            self.last_shot = pygame.time.get_ticks()
        
        


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
                    print "increasing"
                else:
                    item_choice = 1



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
    print "itemNum=",itemNum
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


    
        
            
