import pygame
import random
import sprites
import os
from random import randint

pygame.init()

screen_height = 650
screen_width = 350
window_height = 1080
window_width = 1920
size = (screen_height, screen_width)
screen = pygame.display.set_mode(size)

pos_x = screen_width / 2 - window_width / 2
pos_y = screen_height - window_height
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '1'

background_image = pygame.image.load("graphics/background.jpg").convert()

hitmob = pygame.mixer.Sound("sound/HitMob.wav")
hit1 = pygame.mixer.Sound("sound/Hit1.wav")
hit2 = pygame.mixer.Sound("sound/Hit2.wav")

title = pygame.image.load("graphics/title.png")
how2play = pygame.image.load("graphics/h2p.png")

pygame.mixer.init()
pygame.display.set_caption('Flugel')

gameDisplay = pygame.display.set_mode((screen_width, screen_height))
game_rect = gameDisplay.get_rect()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bullets_boss = pygame.sprite.Group()
bullets_mobs = pygame.sprite.Group()
boss = pygame.sprite.Group()
player = sprites.character()
Boss1 = sprites.boss1()
Boss2 = sprites.boss2()
all_sprites.add(player)

def newmob1(x, y):
    r = random.randrange(x, y)
    for i in range(r):
        m = sprites.monster()
        mobs.add(m)
        all_sprites.add(m)
def newmob2(x, y):
    r = random.randrange(x, y)
    for i in range(r):
        m2 = sprites.monster2()
        mobs.add(m2)
        all_sprites.add(m2)
def newmob3():
    m3 = sprites.monster3()
    mobs.add(m3)
    all_sprites.add(m3)

def load_img(img ,x, y):
    gameDisplay.blit(img, (x, y));

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button_ret(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
            return False
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    return True

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def intro():
  starting = True
  while starting:
    clock.tick(60)
    screen.blit(background_image, [0, 0]) #activates background
    load_img(title,50,150)
    button("How to play", 110, 400, 150, 50, red, green, h2p)
    starting = button_ret("Start", 135, 300, 100, 50, red, green, game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting = False
    pygame.display.flip()

def game():
  score = 0
  p = 0
  print('Score :', score)
  running = True
  spawn_boss1 = True
  spawn_boss2 = True
  boss_dead = False
  hpboss1 = 50
  hpboss2 = 50
  pygame.mixer.music.load("sound/BGM.wav")
  pygame.mixer.music.play(-1)
  
  while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    p = p + 1
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    bosshits = pygame.sprite.groupcollide(boss, bullets, boss_dead, True)    
    if score < 1000:
      if p//60 == 1:
        newmob1(2, 4)
        p = 0    
    elif score >= 1000 and score < 1500 :
      if p//60 == 1:
        newmob2(1, 3)
        p = 0
    elif score >= 3000 and score < 4500:
      if p//120 == 1:
        newmob1(0,3)
        newmob2(0,2)
        newmob3()
        p = 0
    elif score >= 4500:
      if p//360 == 1 and spawn_boss2:
        boss.add(Boss2)
        all_sprites.add(Boss2)
        spawn_boss2 = False
        print('Boss HP: ', hpboss2)
      for bosshit in bosshits:
        hit2.play()
        hpboss2 -= 1
        print('Boss HP: ', hpboss2)
        if hpboss2 == 0:
          score += 1500
          p = 0
          print('Score: ', score)
          print('Thank you for playing!')
      if hpboss2 == 1:
        boss_dead = True
    elif score >= 1500:
      if p//360 == 1 and spawn_boss1:
        boss.add(Boss1)
        all_sprites.add(Boss1)
        spawn_boss1 = False
        print('Boss HP: ', hpboss1)
      for bosshit in bosshits:
        hit1.play()
        hpboss1 -= 1
        print('Boss HP: ', hpboss1)
        if hpboss1 == 0:
          score += 1500
          p = 0
          print('Get Ready For Round 2!')
          boss_dead = False
          print('Score: ', score)
      if hpboss1 == 1:
        boss_dead = True
    for hit in hits:
        hitmob.play()
        score += 100
        print('Score: ', score)
    player_hits1 = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if player_hits1:
        print('Game Over')
        running = False
    player_hits2 = pygame.sprite.spritecollide(player, bullets_boss, False, pygame.sprite.collide_circle)
    if player_hits2:
        print('Game Over')
        running = False
    player_hits3 = pygame.sprite.spritecollide(player, bullets_mobs, False, pygame.sprite.collide_circle)
    if player_hits3:
        print('Game Over')
        running = False
    # Draw / render
    screen.blit(background_image, [0, 0]) #activates background
    all_sprites.draw(gameDisplay)
    pygame.display.flip()

def h2p():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, [0, 0])
        load_img(how2play, 50, 50)
        #running = button_ret("Back", 110, 400, 150, 50, red, green, intro)
        pygame.display.flip()
