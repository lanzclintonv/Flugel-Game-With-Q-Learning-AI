import pygame
import keras
from keras.models import load_model
import functions
import numpy as np
import math
import sprites
import random
import os
from random import randint

class Neuralnetwork():
    def __init__(self):
       self.boss_miss = []
       self.model = load_model("test_model_v1.h5")
       
       
    def get_data(self,training_data,c):
       character_hit = pygame.sprite.spritecollide(dummy, bullets_boss, True, pygame.sprite.collide_circle)
       boss_move = []
       bullet_miss = False
       
       player_distance = self.get_playerpos()
       boss_miss = 0
       bullet_boss1 = Bullet_Boss1(Boss1.rect.centerx, Boss1.rect.bottom)       #for i in range(self.turns):
       boss_move = self.get_action(Boss1.move,player_distance)
    
       
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
       return training_data
    
    def get_action(self,x,y,z):
       #print(x)
       #print(y)
       return np.array([x,y,z])
             
    def get_playerpos(self):
       player_pos = [functions.player.rect.x, functions.player.rect.y]
       boss_pos = [functions.Boss1.rect.x, functions.Boss1.rect.y]
       los = math.atan2(player_pos[0] - boss_pos[0], player_pos[1] - boss_pos[1]) / np.pi
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

    def test_model(self,move,speed):
       angle = self.get_playerpos()
       move = self.model.predict(self.get_action(functions.Boss1.move,functions.Boss1.speedx,angle).reshape(1,3))
       print(move)
       return move

