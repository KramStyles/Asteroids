import pygame, os, sys, math
from pygame.locals import *

from random import randint

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
ship_moving = pygame.image.load(os.path.join('images', 'ship_thrusted.png'))
asteroids = pygame.image.load(os.path.join('images', 'asteroid.png'))

ship_angle = 90
ship_is_rotating = False
ship_is_forward = False
ship_direction = 0
ship_x = Width / 2 - (ship.get_width() / 2)
ship_y = Height / 2 - (ship.get_height() / 2)
ship_speed = 0

asteroids_x = []
asteroids_y = []
no_asteroids = 5
asteroids_angle = []
asteroids_speed = []

for i in range(0, no_asteroids):
    asteroids_x.append(randint(0, Width))
    asteroids_y.append(randint(0, Height))
    asteroids_angle.append(randint(0, 365))
    asteroids_speed.append(randint(1, 3))


def rotate_image(image, angle):
    orig_rec = image.get_rect()
    rot_img = pygame.transform.rotate(image, angle)
    rot_rec = orig_rec.copy()
    rot_rec.center = rot_img.get_rect().center
    rot_img = rot_img.subsurface(rot_rec).copy()
    return rot_img


# Draw game function
def draw(canvas):
    global Time, ship_is_forward
    canvas.fill(Black)
    canvas.blit(bg, (0, 0))
    canvas.blit(debris, (Time * .3, 0))
    canvas.blit(debris, (Time * .3 - Width, 0))

    for i in range(0, no_asteroids):
        canvas.blit(rotate_image(asteroids, Time), (asteroids_x[i], asteroids_y[i]))

    if ship_is_forward:
        canvas.blit(rotate_image(ship_moving, ship_angle), (ship_x, ship_y))
    else:
        canvas.blit(rotate_image(ship, ship_angle), (ship_x, ship_y))

    Time += 2  # Code causing the debris to move


# Handle Keyboard Input
def handle_input():
    global ship_angle, ship_direction, ship_is_rotating, ship_y, ship_x
    global ship_is_forward, ship_speed
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
            elif event.key == K_UP:
                ship_is_forward = True
                ship_speed = 10
        elif event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                ship_is_forward = False
            else:
                ship_is_rotating = False

    if ship_is_rotating:
        if ship_direction == 1:
            ship_angle -= 10
        else:
            ship_angle += 10

    if ship_is_forward or ship_speed > 0:
        ship_x += math.cos(math.radians(ship_angle)) * ship_speed
        ship_y += -math.sin(math.radians(ship_angle)) * ship_speed
        if not ship_is_forward:
            ship_speed -= 0.3


# Update Screen
def update_screen():
    pygame.display.update()
    fps.tick(60)


# Game Logic
def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 25:
        print(distance)
        return True
    else:
        return False


def game_logic():
    for i in range(0, no_asteroids):
        asteroids_x[i] += math.cos(math.radians(asteroids_angle[i])) * asteroids_speed[i]
        asteroids_y[i] += -math.sin(math.radians(asteroids_angle[i])) * asteroids_speed[i]

        if asteroids_y[i] < 0:  # When height of asteroid is less than 0 (out of screen position)
            asteroids_y[i] = Height  # The height is returned to the other position

        if asteroids_x[i] < 0:
            asteroids_x[i] = Width

        if asteroids_y[i] > Height:
            asteroids_y[i] = 0

        if asteroids_x[i] > Width:
            asteroids_x[i] = 0

        if isCollision(ship_x, ship_y, asteroids_x[i], asteroids_y[i]):
            print('Game Over')
            exit()


# Pygame is like a running loop
while True:
    draw(window)
    handle_input()
    game_logic()
    update_screen()
