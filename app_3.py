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
ship = pygame.image.load(os.path.join('images', 'ship.png'))

ship_angle = 90
ship_is_rotating = False
ship_direction = 0


def rotate_image(image, angle):
    orig_rec = image.get_rect()
    rot_img = pygame.transform.rotate(image, angle)
    rot_rec = orig_rec.copy()
    rot_rec.center = rot_img.get_rect().center
    rot_img = rot_img.subsurface(rot_rec).copy()
    return rot_img


# Draw game function
def draw(canvas):
    global Time
    canvas.fill(Black)
    canvas.blit(bg, (0, 0))
    canvas.blit(debris, (Time * .3, 0))
    canvas.blit(debris, (Time * .3 - Width, 0))

    canvas.blit(rotate_image(ship, ship_angle), ((Width / 2 - (ship.get_width() / 2)), (Height / 2 - (ship.get_height() / 2))))

    Time += 2  # Code causing the debris to move


# Handle Keyboard Input
def handle_input():
    global ship_angle, ship_direction, ship_is_rotating
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                ship_is_rotating = True
                ship_direction = 0
            elif event.key == K_RIGHT:
                ship_is_rotating = True
                ship_direction = 1
        elif event.type == KEYUP:
            ship_is_rotating = False

    if ship_is_rotating:
        if ship_direction == 1:
            ship_angle -= 10
        else:
            ship_angle += 10


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
    # game_logic()
    update_screen()
