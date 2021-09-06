import pygame, os, sys, random, math
from pygame.locals import *

pygame.init()
# We record the frames per second
fps = pygame.time.Clock()

# We define our colours

White = (245, 245, 245)
Green = (50, 205, 50)
Blue = (30, 144, 255)
Red = (220, 20, 60)
Black = (14, 14, 14)

# Globals
Width = 800
Height = 600
Time = 0

# Canvas Declaration
window = pygame.display.set_mode((Width, Height), 0, 32)
pygame.display.set_caption('My Asteroids Game')

# Load Images
bg = pygame.image.load(os.path.join('images', 'bg.jpg'))
debris = pygame.image.load(os.path.join('images', 'debris2_brown.png'))


# Draw game function
def draw(canvas):
    global Time
    canvas.fill(Black)
    canvas.blit(bg, (0, 0))
    canvas.blit(debris, (Time * .3, 0))
    canvas.blit(debris, (Time * .3 - Width, 0))

    Time += 1  # Code causing the debris to move


# Handle Keyboard Input
def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


# Update Screen
def update_screen():
    pygame.display.update()
    fps.tick(60)


# Game Login
def game_logic():
    pass


# Pygame is like a running loop
while True:
    draw(window)
    handle_input()
    game_logic()
    update_screen()
