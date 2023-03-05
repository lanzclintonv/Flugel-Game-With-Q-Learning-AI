import pygame
import os

pygame.init()

screen_height = 650
screen_width = 350
window_height = 1080
window_width = 1920
size = (screen_height, screen_width)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("graphics/background.jpg").convert()
pos_x = screen_width / 2 - window_width / 2
pos_y = screen_height - window_height
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.init()
pygame.display.set_caption('Flugel')

title = pygame.image.load("graphics/title.png")
scores = pygame.image.load("graphics/SCORE.png")

gameDisplay = pygame.display.set_mode((screen_width, screen_height))
game_rect = gameDisplay.get_rect()

clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def load_image(img,x, y):
    gameDisplay.blit(img, (x, y));

def text_objects(color, text, font):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',32)
    TextSurf, TextRect = text_objects(blue, text, largeText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)

def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(black, msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background_image, [0, 0]) #activates background
    button("Start", 135, 350, 100, 50, red, green)
    load_image(title,50,200)
    #load_image(scores, 100, 100)
    message_display('Score', 50, 625)
    pygame.display.flip()

pygame.quit()
