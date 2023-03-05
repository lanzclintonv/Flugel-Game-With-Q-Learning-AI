#model for easy difficulty

import tensorflow
import math
#import grab_screen from grabscreen
import pygame
import numpy as np
import random
from random import randint
from keras.models import load_model
import time
import keras
import os

screen_height = 650
screen_width = 350 #700
screen_game_width = 350
window_height = 1080
window_width = 1920
size = (screen_height, screen_width)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("background.jpg").convert()
pos_x = screen_width / 2 - window_width / 2
pos_y = screen_height - window_height
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '1'

player_1 = pygame.image.load('player.png')
moveRight = pygame.image.load('player_right.png')
moveLeft = pygame.image.load('player_left.png')
boss_1 = pygame.image.load('boss_temp.png')
bullet_boss1 = pygame.image.load('bullet_boss1.png')
bullet_boss1 = pygame.transform.scale(bullet_boss1, (30,30))

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((screen_width, screen_height))
game_rect = gameDisplay.get_rect()

class play(object):
   def update(gatherdata):
       keystate = pygame.key.get_pressed()
       if keystate[pygame.K_z] and gatherdata == False:
           gatherdata = True
           for i in range(2):
              time.sleep(1)
              print(i)
       #elif keystate[pygame.K_z] and gatherdata == True:
           #gatherdata = False              
       return gatherdata
   def updateonce(gatherdata):
       keystate = pygame.key.get_pressed()
       if keystate[pygame.K_x]:
           gatherdata = True
           for i in range(2):
              time.sleep(1)
              print(i)
           #im = ImageGrab.grab(bbox=(785,226,1135,876))
           #
           #im.save("sample.jpg")
           #print("Image Saved!")
       return gatherdata
	#def running(play):


class boss1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_1
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = -20
        self.speedy = 0
        r = veryrand()
        self.speedx = 3
        self.move = 1
        self.shoots = r
        self.bulletDelay = 400
        self.shot = pygame.time.get_ticks()
        self.bullet_instance = []
        
    def update(self):
        bullet_boss1 = Bullet_Boss1(self.rect.centerx, self.rect.bottom)
        self.rect.x += self.speedx
        #self.rect.y += self.speedy

        self.shoots = nn.test_model()
        if self.shoots > 0.5:
           Boss1.shoot()
        #if self.shoots == 1:
           #Boss1.shoot()
        #self.shoots = veryrand()
        
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
            all_sprites.add(bullet_boss1)
            bullets_boss.add(bullet_boss1)
            self.bullet_instance = np.append(self.bullet_instance,1)

class Bullet_Boss1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_boss1
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10
        self.boss_miss = []
        self.miss_length = 0

    def update(self):
        #print(self.gone)
        self.rect.y += self.speedy
        self.miss_length = len(self.boss_miss)
        if self.rect.top > screen_height - 50: #+ 10:
            self.kill()
            nn.boss_miss = np.append(nn.boss_miss,1)
            self.miss_length = self.miss_length + 1

class character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_1
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_game_width / 2
        self.rect.bottom = screen_height - 10
        self.speedx = 0
        self.speedy = 0
        self.radius = 18
        self.bulletDelay = 1200
        self.shot = pygame.time.get_ticks()

    #def rand(self):


    def update(self):

        self.speedx = 0
        self.speedy = 0
        character_hit = pygame.sprite.spritecollide(dummy, bullets_boss, True, pygame.sprite.collide_circle)
        #character_ram = pygame.sprite.groupcollide(character, boss1, True, True)
        
        if self.rect.right > screen_game_width:
            self.rect.right = screen_game_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top <= 250:
            self.rect.top = 250
    def move(self):
         self.rect = self.image.get_rect()
         self.rect.x = random.randrange(screen_width - self.rect.width)
         self.rect.y = random.randrange(screen_height - self.rect.height)        
     #def spawnchara:
         #r =
         #all_sprites.add(dummy)
         
class Neuralnetwork():
    def __init__(self):
       self.boss_miss = []
       self.model = load_model("test_model_v1.h5")
       
       
    def get_data(self,training_data,c):
       character_hit = pygame.sprite.spritecollide(dummy, bullets_boss, True, pygame.sprite.collide_circle)
       boss_move = []
       bullet_miss = False
       
       #all_sprites.update()
       player_distance = self.get_playerpos()
       boss_miss = 0
       bullet_boss1 = Bullet_Boss1(Boss1.rect.centerx, Boss1.rect.bottom)
       #all_sprites.update()
       #for i in range(self.turns):
       boss_move = self.get_action(Boss1.move,Boss1.speedx,player_distance)
       #print(Boss1.speedx)
          
          #player_distance = self.get_playerpos(Boss1, dummy)
       #bullet_miss = check_bullet()
       
       bullet_instance = len(Boss1.bullet_instance)
       
       if len(self.boss_miss) > 1:#len(bullet_boss1.boss_miss) > bullet_boss1.miss_length:
          training_data.append([boss_move, -1])
          #print("miss")
          self.boss_miss = []
          
       #if boss_miss == True:
       elif character_hit or (player_distance <= 0.08 and player_distance >= -0.08):
          training_data.append([boss_move, 1])
          if character_hit:
             boss_miss = 0
             dummy.move()
       else:
          training_data.append([boss_move, 0])
       #print(len(self.boss_miss))
       #print(training_data[c][1])
       #print(bullet_instance)
       #print(bullet_boss1.boss_miss)
       return training_data
    
    def get_action(self,move,bossvel,playerpos):
       #print(x)
       #print(y)
       bossvel = bossvel / 5
       return np.array([move,bossvel,playerpos])
             
    def get_playerpos(self):#player_boss, character):
       dummy_pos = [dummy.rect.x, dummy.rect.y]
       boss_pos = [Boss1.rect.x, Boss1.rect.y]
       los = math.atan2(dummy.rect.x - Boss1.rect.x, dummy.rect.y - Boss1.rect.y) / np.pi#self.get_angle(boss_pos, dummy_pos)
       #print(los)
       return los

    def check_bullet(self,c):
       miss = False
       if len(c) > 0:
          miss = True
       #print(miss)
       return miss
      
    def get_angle(self,x,y):
       x = self.normalize_vector(x)
       y = self.normalize_vector(y)
       return math.atan2(x[0] * y[1] - x[1] * y[0], x[0] * y[0] - x[1] * y[1]) / np.pi
      
    def normalize_vector(self,x):
       return x / np.linalg.norm(x)

    def test_model(self):
       x = self.get_playerpos()
       move = self.model.predict(self.get_action(Boss1.move,Boss1.speedx,x).reshape(1,3))
       print(move)
       return move

def veryrand():
  exclude=[0]
  randInt = randint(-1, 1)
  return veryrand() if randInt in exclude else randInt

def veryrandmove():
  exclude=[0]
  randInt = randint(-5, 5)
  return veryrand() if randInt in exclude else randInt
#def check_run():
   
def game():
    running = True
    spawn_boss1 = True
    training_data = []
    dataset = []
    gatherdata = False
    runs = 0
    
    turns = 0
    allturns = 0
    c = 0


    while running:
      clock.tick(60)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False

      screen.blit(background_image, [0, 0])
      all_sprites.draw(gameDisplay)
      pygame.display.flip()

      character_hit = pygame.sprite.spritecollide(dummy, bullets_boss, True, pygame.sprite.collide_circle)
      
      all_sprites.update()
      #print(pygame.time.get_ticks())
      #print(clock.get_time() / 1000.0)

      if character_hit:
         dummy.move()
      #nn.test_model()

      if gatherdata:
        dataset = nn.get_data(dataset,turns)
        #print(len(dataset))
        #print(dataset[allturns][1])
        turns = turns + 1
        
      #if dataset[allturns][1] == -1 or turns == 1000:
         #print("cut")
         #print(dataset[allturns][1])
         #runs = runs + 1
         #turns = 0
         #print("[{}]".format(runs))
      #allturns = allturns + 1
      #if runs == 5000:
       # np.save("training_data_vel.npy",dataset)
        #print("Saved!")
       # gatherdata = False
      
      #bosshits = pygame.sprite.spritecollide(dummy, bullets_boss, True, pygame.sprite.collide_circle)
      screen.blit(background_image, [0, 0])
      all_sprites.draw(gameDisplay)
      pygame.display.flip()
      
all_sprites = pygame.sprite.Group()
bullets_boss = pygame.sprite.Group()
boss = pygame.sprite.Group()
dummy = character()
Boss1 = boss1()
nn = Neuralnetwork()
all_sprites.add(dummy)
all_sprites.add(Boss1)

game()





#def controlqueue():
        


           
#mpl.imshow(np.squeeze(trainingdata[10]))
#mpl.show()

