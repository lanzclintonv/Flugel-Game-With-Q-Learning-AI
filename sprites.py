import pygame
import random
import functions
import keras
from Neuralnetwork import Neuralnetwork
from random import randint

screen_height = 650
screen_width = 350
window_height = 1080
window_width = 1920

player_1 = pygame.image.load("graphics/player.png")
moveRight = pygame.image.load("graphics/player_right.png")
moveLeft = pygame.image.load("graphics/player_left.png")
enemy_1 = pygame.image.load("graphics/monster 1.png")
enemy_2 = pygame.image.load("graphics/monster 2.png")
enemy_3 = pygame.image.load("graphics/monster 3.png")
boss_1 = pygame.image.load("graphics/boss1.png")
boss_2 = pygame.image.load("graphics/boss2.png")
bullet = pygame.image.load("graphics/bullet.png")
bullet = pygame.transform.scale(bullet, (30,30))
bullet_boss1 = pygame.image.load("graphics/bullet_boss1.png")
bullet_boss1 = pygame.transform.scale(bullet_boss1, (30,30))
bullet_boss2 = pygame.image.load("graphics/bullet_boss2.png")
bullet_boss2 = pygame.transform.scale(bullet_boss2, (30,30))
bullet_monster = pygame.image.load("graphics/bullet_monster.png")
bullet_monster = pygame.transform.scale(bullet_monster, (30,30))

def veryrand():
  exclude=[0]
  randInt = randint(-2, 2)
  return veryrand() if randInt in exclude else randInt

def veryrandmove():
  exclude=[0]
  randInt = randint(-5, 5)
  return veryrand() if randInt in exclude else randInt

class character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_1
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height - 10
        self.speedx = 0
        self.speedy = 0
        self.radius = 18
        self.bulletDelay = 400
        self.shot = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.image = moveLeft
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.image = moveRight
        self.rect.x += self.speedx
        if keystate[pygame.K_UP]:
            self.speedy = -8
            self.image = player_1
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
            self.image = player_1
        self.rect.y += self.speedy
        if keystate[pygame.K_SPACE]:
            functions.player.shoot()
            self.image = player_1
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top <= 200:
            self.rect.top = 200

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shot > self.bulletDelay:
            self.shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            functions.all_sprites.add(bullet)
            functions.bullets.add(bullet)

class monster(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_1
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)
        self.radius = 25
        self.speedx = 0
        self.health = 100

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > screen_height + 10 or self.rect.left < -25 or self.rect.right > screen_width + 20:
            #self.rect.x = random.randrange(screen_width - self.rect.width)
            #self.rect.y = random.randrange(-100, -40)
            #self.speedy = random.randrange(1, 3)
            self.kill
        
class monster2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_2
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(50)
        self.speedy = random.randrange(1, 3)
        self.radius = 25
        self.speedx = random.randrange(-3, 3) #sets random movements

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > screen_height + 10:
            self.kill
        if self.rect.left < -25:
            self.rect.left = 0
            self.speedx += 5
        if self.rect.right > screen_width + 20:
            self.rect.right = screen_width
            self.speedx -= 5

class monster3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_3
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(50)
        self.speedy = 2
        self.radius = 25
        self.speedx = random.randrange(-3, 3)
        self.shot = pygame.time.get_ticks()
        self.bulletDelay = 600

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.shoot()
        if self.rect.top >= 100:
            self.rect.top = 100
        if self.rect.left < -25:
            self.rect.left = 0
            self.speedx += 5
        if self.rect.right > screen_width + 20:
            self.rect.right = screen_width
            self.speedx -= 5

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shot > self.bulletDelay:
            self.shot = now
            bullet_mobs = Bullet_Monster(self.rect.centerx, self.rect.bottom)
            functions.all_sprites.add(bullet_mobs)
            functions.bullets_mobs.add(bullet_mobs)
            
class boss1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_1
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = -20
        self.speedy = 0
        r = veryrand()
        self.move = 1
        self.speedx = r
        self.shoots = r
        self.bulletDelay = 600
        self.shot = pygame.time.get_ticks()
        self.dodged = pygame.time.get_ticks()
        self.dodgeDelay = 1000
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.shoots = n.test_model(self.move,self.speedx)
        if self.shoots > 0.5:
            functions.Boss1.shoot()
        if self.rect.left < -25:
            self.rect.left = 0
            self.speedx = abs(veryrandmove()) 
            self.move = 1
        if self.rect.right > screen_width + 20:
            self.rect.right = screen_width
            #r = veryrand()
            self.speedx = -abs(veryrandmove())
            self.move = -1 

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shot > self.bulletDelay:
            self.shot = now
            bullet_boss1 = Bullet_Boss1(self.rect.centerx, self.rect.bottom)
            functions.all_sprites.add(bullet_boss1)
            functions.bullets_boss.add(bullet_boss1)

    def dodge(self):
      time = pygame.time.get_ticks()
      if time - self.dodged > self.dodgeDelay:
        self.dodged = time
        x = functions.player.rect.centerx
        limx1 = x + 90
        limx2 = x - 90
        if(self.rect.centerx <= limx1 and self.rect.centerx >= limx2):
          r = random.randrange(-4, 4)
          if(self.speedx >= 0):
            self.speedx = r
            print('Dodged')
          else:
            self.speedx = r
            print('Dodged')

class boss2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_2
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = -20
        self.speedy = 0
        r = veryrand()
        self.shoots = r
        self.speedx = r
        self.bulletDelay = 600
        self.shot = pygame.time.get_ticks()
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.shoots = n.test_model(self.move,self.speedx)
        if self.shoots > 0.5:
            functions.Boss1.shoot()
        if self.rect.left < -25:
            self.rect.left = 0
            self.speedx = abs(veryrandmove()) 
            self.move = 1
        if self.rect.right > screen_width + 20:
            self.rect.right = screen_width
            #r = veryrand()
            self.speedx = -abs(veryrandmove())
            self.move = -1 

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.shot > self.bulletDelay:
            self.shot = now
            bullet_boss2 = Bullet_Boss2(self.rect.centerx, self.rect.bottom)
            functions.all_sprites.add(bullet_boss2)
            functions.bullets_boss.add(bullet_boss2)
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Bullet_Boss1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_boss1
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > screen_height + 10:
            self.kill()

class Bullet_Boss2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_boss2
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > screen_height + 10:
            self.kill()

class Bullet_Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_monster
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > screen_height + 10:
            self.kill()


n = Neuralnetwork()
