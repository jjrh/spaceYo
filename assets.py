import pygame
import random
import math
from helper import *
from gameGlobals import *


"""
ship, aka the player.
In the future we might want to use this as the base for
the ai as well. 

"""
class ship(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("ship.png")

        self.image_normal = self.image
        self.image_normal = pygame.transform.scale(self.image_normal, (32,32))
        self.rect = self.image_normal.get_rect()
        self.image_left, self.rect_left = load_image("ship_left.png")
        self.image_left = pygame.transform.scale(self.image_left, (32,32))
        self.image_right, self.rect_right = load_image("ship_right.png")
        self.image_right = pygame.transform.scale(self.image_right, (32,32))
        
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.timer = pygame.time.get_ticks()

        self.rate = 10

        self.particles = pygame.sprite.Group()
        self.max_particles = 30

        self.bullets = pygame.sprite.Group()
        self.bullet_speed = 1
        self.bullet_rate = 100 # in mili seconds
        self.shoot = False
        self.last_shot = self.timer

        self.HP = 10
        

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

        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()


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


        self.force_ai = 0

        self.ai_choice = random.randint(1,2)
        self.ai_choice_timer =pygame.time.get_ticks()
    def update(self):

        if self.force_ai ==0:
            if (pygame.time.get_ticks() - self.ai_choice_timer) > 500:
                self.ai_choice = random.randint(1,2)
                self.ai_choice_timer = pygame.time.get_ticks()
            if self.ai_choice == 1:
                self.shooting_ai_1()
            if self.ai_choice == 2:
                self.shooting_ai_2()
        else:
           
            if self.force_ai == 1:
                self.ai1()
            elif self.force_ai == 2:
                self.ai2()
            elif self.force_ai == 3:
                self.ai3()
            elif self.force_ai == 4:
                self.ai4()
            else:
                print "ERROR AI NOT DEFINED"
                
            
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

    # moves the character across and shoots.
    def shooting_ai_1(self):

        if(pygame.time.get_ticks() - self.last_direction_change) > 500:
            self.direction = self.direction*-1
            self.last_direction_change = pygame.time.get_ticks()
        
        self.rect = self.rect.move(self.direction*self.speed,1)
        if self.rect.centerx > WINX:
            self.direction = -1
        if self.rect.centerx < 0:
            self.direction = 1
        self.shoot_mechanic()

    # just moves the character down the screen
    def shooting_ai_2(self):
        self.rect = self.rect.move(0,self.speed)

        # Check the particles to see if they have left the viewable area on the screen
        # if they have we remove them from the group and kill them.

    def ai1(self):
        self.shooting_ai_1()
    def ai2(self):
        self.shooting_ai_2()

    # slow move
    def ai3(self):
        self.rect = self.rect.move(0, self.speed/2)

    # move down and shoot
    def ai4(self):
        self.rect = self.rect.move(0, self.speed/2)
        self.shoot_mechanic_random()

    def shoot_mechanic_random(self):
        if (pygame.time.get_ticks() - self.last_shot) > self.bullet_rate:
            if random.randint(1,2) == 2:
                self.bullets.add(bullet((0,self.bullet_speed), self.rect.center))
            self.last_shot = pygame.time.get_ticks()

    
    def shoot_mechanic(self):
        if (pygame.time.get_ticks() - self.last_shot) > self.bullet_rate:
            self.bullets.add(bullet((0,self.bullet_speed), self.rect.center))
            self.last_shot = pygame.time.get_ticks()
