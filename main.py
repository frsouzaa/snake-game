import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 827  # 828 no total, a tela começa no 0
SCREEN_HEIGHT = 647  # 648 no total, a tela começa com 0
pixels = 3

# Site para criar as spites
# https://www.pixilart.com/draw?gclid=CjwKCAjwmJeYBhAwEiwAXlg0AbIKMpZRreBF0OZQnGkZP6KjKjkZgWNPZbxQKKomkeUSt_EGgjbVpxoC6o4QAvD_BwE#
if random.randint(0, 2) == 0:
    snakeColor = (255, 211, 68)  # amarelo
    head = pygame.image.load(r'imgs/yellow.png')
else:
    snakeColor = (57, 110, 154)  # azul
    head = pygame.image.load(r'imgs/blue.png')

background = pygame.image.load(r'imgs/fundo.png')

class Body(pygame.sprite.Sprite):
    def __init__(self):
        super(Body, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill(snakeColor)
        self.rect = self.body.get_rect()
        self.direction = 0


class Curva(pygame.sprite.Sprite):
    def __init__(self):
        super(Curva, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill(snakeColor)
        self.rect = self.body.get_rect()
        self.colliding = False


class Point(pygame.sprite.Sprite):
    def __init__(self):
        super(Point, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill((254, 90, 90))
        self.rect = self.body.get_rect()
        self.colliding = False


def move():
    global body
    global pixels
    for k in range(1, len(body)):
        if (body[k].rect[1] > body[k - 1].rect[1] and body[k].rect[0] == body[k - 1].rect[0]) or \
                (body[k].rect[1] > body[k - 1].rect[1] and body[k - 1].direction != 1):
            body[k].rect.move_ip(0, -pixels)
            body[k].direction = 1
        elif (body[k].rect[1] < body[k - 1].rect[1] and body[k].rect[0] == body[k - 1].rect[0]) or \
                (body[k].rect[1] < body[k - 1].rect[1] and body[k - 1].direction != 2):
            body[k].rect.move_ip(0, pixels)
            body[k].direction = 2
        elif (body[k].rect[0] > body[k - 1].rect[0] and body[k].rect[1] == body[k - 1].rect[1]) or \
                (body[k].rect[0] > body[k - 1].rect[0] and body[k - 1].direction != 3):
            body[k].rect.move_ip(-pixels, 0)
            body[k].direction = 3
        else:
            body[k].rect.move_ip(pixels, 0)
            body[k].direction = 4


def changedirection(d):
    global body
    global curva
    global direction
    global head
    if body[0].direction == 1 and d == 3:
        head = pygame.transform.rotate(head, 90)
    elif body[0].direction == 1 and d == 4:
        head = pygame.transform.rotate(head, -90)
    elif body[0].direction == 2 and d == 3:
        head = pygame.transform.rotate(head, -90)
    elif body[0].direction == 2 and d == 4:
        head = pygame.transform.rotate(head, 90)
    elif body[0].direction == 3 and d == 1:
        head = pygame.transform.rotate(head, -90)
    elif body[0].direction == 3 and d == 2:
        head = pygame.transform.rotate(head, 90)
    elif body[0].direction == 4 and d == 1:
        head = pygame.transform.rotate(head, 90)
    elif body[0].direction == 4 and d == 2:
        head = pygame.transform.rotate(head, -90)

    body[0].direction = d
    direction = d
    curva.append(Curva())
    curva[-1].rect.update(body[0].rect[0], body[0].rect[1], 30, 30)
    screen.blit(curva[-1].body, curva[-1].rect)


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

body = [Body(), Body(), Body()]
curva = []
point = Point()

body[0].rect.update(396+3, SCREEN_HEIGHT / 2, 30, 30)
body[1].rect.update(396+3, SCREEN_HEIGHT / 2 + 30, 30, 30)
body[2].rect.update(396+3, SCREEN_HEIGHT / 2 + 60, 30, 30)
point.rect.update(random.randint(1, 782), random.randint(1, 633), 30, 30)

running = True

clock = pygame.time.Clock()

lastKey = [None, None]
direction = None
pressedKey = None
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[K_UP] and lastKey[0] != 2 and lastKey[0] != 1:
        lastKey[0] = 1
    if pressedKeys[K_DOWN] and lastKey[0] != 1 and lastKey[0] != 2:
        lastKey[0] = 2
    if pressedKeys[K_LEFT] and lastKey[0] != 4 and lastKey[0] != 3:
        lastKey[0] = 3
    if pressedKeys[K_RIGHT] and lastKey[0] != 3 and lastKey[0] != 4:
        lastKey[0] = 4

    if frame == 12:
        pressedKeys = pygame.key.get_pressed()
        if lastKey[0] == 1 and body[0].direction != 1 and body[0].direction != 2:
            changedirection(1)
        if lastKey[0] == 2 and body[0].direction != 2 and body[0].direction != 1:
            changedirection(2)
        if lastKey[0] == 3 and body[0].direction != 3 and body[0].direction != 4:
            changedirection(3)
        if lastKey[0] == 4 and body[0].direction != 4 and body[0].direction != 3:
            changedirection(4)
        frame = 0

    frame = frame + 1

    if direction == 1:
        body[0].rect.move_ip(0, -pixels)
        move()
    elif direction == 2:
        body[0].rect.move_ip(0, pixels)
        move()
    elif direction == 3:
        body[0].rect.move_ip(-pixels, 0)
        move()
    elif direction == 4:
        body[0].rect.move_ip(pixels, 0)
        move()

    for i in range(2, len(body)):
        if pygame.Rect.colliderect(body[0].rect, body[i].rect):
            running = False

    if pygame.Rect.colliderect(point.rect, body[0].rect):
        point.rect.update(random.randint(0, 24)*36+3, random.randint(0, 19)*36+3, 30, 30)
        point.colliding = False
        i = 0
        while i < len(body) and not point.colliding:
            if pygame.Rect.colliderect(point.rect, body[i].rect):
                point.colliding = True
                point.rect.update(random.randint(1, 782), random.randint(1, 633), 30, 30)
            else:
                point.colliding = False
            i = i + 1

        body.append(Body())
        if body[-2].direction == 1:
            body[-1].rect.update(body[len(body) - 2].rect[0], body[len(body) - 2].rect[1] + 30, 30, 30)
            body[-1].direction = 1
        elif body[-2].direction == 2:
            body[-1].rect.update(body[len(body) - 2].rect[0], body[len(body) - 2].rect[1] - 30, 30, 30)
            body[-1].direction = 2
        elif body[-2].direction == 3:
            body[-1].rect.update(body[len(body) - 2].rect[0] + 30, body[len(body) - 2].rect[1], 30, 30)
            body[-1].direction = 3
        else:
            body[-1].rect.update(body[len(body) - 2].rect[0] - 30, body[len(body) - 2].rect[1], 30, 30)
            body[-1].direction = 4

    if body[0].rect[0] >= 798 or body[0].rect[0] <= 1 or body[0].rect[1] >= 648 or body[0].rect[1] <= 1:
        running = False

    # screen.fill((1, 56, 12))

    for i in range(0, 24):
        screen.blit(background, (36*i, 0))
        background = pygame.transform.rotate(background, 180)

    screen.blit(head, body[0].rect)
    for i in range(1, len(body)):
        screen.blit(body[0].body, body[i].rect)

    if len(curva) != 0:
        for i in range(len(curva)):
            curva[i].colliding = False

        i = 0
        while i < len(body) - 1:
            j = 0
            while j < len(curva):
                if pygame.Rect.colliderect(body[i].rect, curva[j].rect):
                    curva[j].colliding = True
                    break
                j = j + 1
            i = i + 1

        i = 0
        while i < len(curva):
            if not curva[i].colliding:
                del curva[i]
            else:
                i = i + 1

        for i in range(len(curva)):
            screen.blit(curva[i].body, curva[i].rect)

    screen.blit(point.body,  point.rect)

    pygame.display.flip()

    clock.tick(70)

pygame.quit()

print("Fim")
