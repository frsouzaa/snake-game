import pygame
from random import randint
from time import sleep

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# https://www.pixilart.com/draw?gclid=CjwKCAjw6raYBhB7EiwABge5Kk8WwnA_64qDUocuIDP4WTjLotw8Bo3sXkXIV30Z3YhwdhIHqHSVKxoCsHYQAvD_BwE#

SCREEN_WIDTH = 828  # 828 no total, a tela começa no 0
SCREEN_HEIGHT = 648  # 648 no total, a tela começa com 0
pixels = 3

color = randint(0, 4)

if color == 0:
    snakeColor = (255, 211, 68)  # amarelo
elif color == 1:
    snakeColor = (57, 110, 154)  # azul
elif color == 2:
    snakeColor = (242, 58, 221)  # rosa
elif color == 3:
    snakeColor = (7, 196, 0)  # verde
elif color == 4:
    snakeColor = (204, 51, 0)  # vermelho

background = pygame.image.load(r'imgs/background.png')
logo = pygame.image.load(r'imgs/logo.png')
gameOver = pygame.image.load(r'imgs/gameover.png')
icon = pygame.image.load(r'imgs/icon.png')


class Body(pygame.sprite.Sprite):
    def __init__(self):
        super(Body, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill(snakeColor)
        self.rect = self.body.get_rect()
        self.direction = 0


class Corner(pygame.sprite.Sprite):
    def __init__(self):
        super(Corner, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill(snakeColor)
        self.rect = self.body.get_rect()
        self.colliding = False


class Point(pygame.sprite.Sprite):
    def __init__(self):
        super(Point, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill((237, 12, 12))
        self.rect = self.body.get_rect()
        self.colliding = False


class LightSquare(pygame.sprite.Sprite):
    def __init__(self):
        super(LightSquare, self).__init__()
        self.body = pygame.Surface((36, 36))
        self.body.fill((64, 64, 64))
        self.rect = self.body.get_rect()


class DarkSquare(pygame.sprite.Sprite):
    def __init__(self):
        super(DarkSquare, self).__init__()
        self.body = pygame.Surface((36, 36))
        self.body.fill((48, 48, 48))
        self.rect = self.body.get_rect()


def move():
    global body
    global pixels
    for k in range(1, len(body)):
        if ((body[k].rect[1] > body[k - 1].rect[1] and body[k].rect[0] == body[k - 1].rect[0]) or
            (body[k].rect[1] > body[k - 1].rect[1] and body[k - 1].direction != 1)) and \
                body[k - 1].direction != DOWN:
            body[k].rect.move_ip(0, -pixels)
            body[k].direction = UP
        elif ((body[k].rect[1] < body[k - 1].rect[1] and body[k].rect[0] == body[k - 1].rect[0]) or
              (body[k].rect[1] < body[k - 1].rect[1] and body[k - 1].direction != 2)) and body[k - 1].direction != UP:
            body[k].rect.move_ip(0, pixels)
            body[k].direction = DOWN
        elif ((body[k].rect[0] > body[k - 1].rect[0] and body[k].rect[1] == body[k - 1].rect[1]) or
              (body[k].rect[0] > body[k - 1].rect[0] and body[k - 1].direction != 3)) and \
                body[k - 1].direction != RIGHT:
            body[k].rect.move_ip(-pixels, 0)
            body[k].direction = LEFT
        elif ((body[k].rect[0] < body[k - 1].rect[0] and body[k].rect[1] == body[k - 1].rect[1]) or
              (body[k].rect[0] < body[k - 1].rect[0] and body[k - 1].direction != 3)) and body[k - 1].direction != LEFT:
            body[k].rect.move_ip(pixels, 0)
            body[k].direction = RIGHT
        elif body[k - 1].direction == UP:
            body[k].rect.move_ip(0, -pixels)
            body[k].direction = UP
        elif body[k - 1].direction == DOWN:
            body[k].rect.move_ip(0, pixels)
            body[k].direction = DOWN
        elif body[k - 1].direction == LEFT:
            body[k].rect.move_ip(-pixels, 0)
            body[k].direction = LEFT
        elif body[k - 1].direction == RIGHT:
            body[k].rect.move_ip(pixels, 0)
            body[k].direction = RIGHT


def change_direction(d):
    global body
    global corners
    global direction

    body[0].direction = d
    direction = d
    corners.append(Corner())
    corners[-1].rect.update(body[0].rect[0], body[0].rect[1], 30, 30)
    screen.blit(corners[-1].body, corners[-1].rect)


def move_square(localx, localy):
    if (localx + localy) % 2 == 0:
        darkSquare.rect.update(localx * 36, localy * 36, 36, 36)
        screen.blit(darkSquare.body, darkSquare.rect)
    else:
        lightSquare.rect.update(localx * 36, localy * 36, 36, 36)
        screen.blit(lightSquare.body, lightSquare.rect)


def load_snake():
    for k in range(0, len(body)):
        screen.blit(body[k].body, body[k].rect)


def set_start_screen(logox, logoy):
    screen.blit(background, (0, 0))
    screen.blit(background, (648, 0))
    screen.blit(logo, (logox, logoy))
    screen.blit(point.body, point.rect)
    load_snake()
    pygame.display.flip()


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Snake")
pygame.display.set_icon(icon)

body = [Body(), Body(), Body()]
corners = []
point = Point()
lightSquare = LightSquare()
darkSquare = DarkSquare()

body[0].rect.update(396 + 3, 399, 30, 30)
body[1].rect.update(396 + 3, 399 + 30, 30, 30)
body[2].rect.update(396 + 3, 399 + 60, 30, 30)
point.rect.update(396 + 3, 108 + 3, 30, 30)

running = True

clock = pygame.time.Clock()

lastKey = None
direction = None
pressedKey = None
frame = 0

set_start_screen(281, 212)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                direction = None
            elif event.key == K_UP:
                running = False
                direction = UP
            elif event.key == K_DOWN:
                running = False
                direction = DOWN
                body[0].rect.update(396 + 3, 399 + 60, 30, 30)
                body[1].rect.update(396 + 3, 399 + 30, 30, 30)
                body[2].rect.update(396 + 3, 399, 30, 30)
                frame = 8
            elif event.key == K_LEFT:
                running = False
                direction = LEFT
            elif event.key == K_RIGHT:
                running = False
                direction = RIGHT
        elif event.type == QUIT:
            running = False
            direction = None

    # Max fps
    clock.tick(67 + len(body))

running = True

set_start_screen(900, 0)

while running and direction is not None:
    # Bloco responsável por fechar o jogo, caso seja precionado esc ou clicado no X ------------------------------------
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    # ------------------------------------------------------------------------------------------------------------------

    # Bloco responsável por ler a ultima tecla pressionada -------------------------------------------------------------
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[K_UP] and lastKey != DOWN and lastKey != UP:
        lastKey = UP
    if pressedKeys[K_DOWN] and lastKey != UP and lastKey != DOWN:
        lastKey = DOWN
    if pressedKeys[K_LEFT] and lastKey != RIGHT and lastKey != LEFT:
        lastKey = LEFT
    if pressedKeys[K_RIGHT] and lastKey != LEFT and lastKey != RIGHT:
        lastKey = RIGHT
    # ------------------------------------------------------------------------------------------------------------------

    # Bloco responsável por mudar a direção da snake -------------------------------------------------------------------
    if frame == 12:
        pressedKeys = pygame.key.get_pressed()
        if lastKey == UP and body[0].direction != UP and body[0].direction != DOWN \
                and 0 < body[0].rect[0] < (SCREEN_WIDTH - 30):
            change_direction(UP)
        if lastKey == DOWN and body[0].direction != DOWN and body[0].direction != UP \
                and 0 < body[0].rect[0] < (SCREEN_WIDTH - 30):
            change_direction(DOWN)
        if lastKey == LEFT and body[0].direction != LEFT and body[0].direction != RIGHT \
                and 0 < body[0].rect[1] < (SCREEN_HEIGHT - 30):
            change_direction(LEFT)
        if lastKey == RIGHT and body[0].direction != RIGHT and body[0].direction != LEFT \
                and 0 < body[0].rect[1] < (SCREEN_HEIGHT - 30):
            change_direction(RIGHT)
        frame = 0

    frame = frame + 1
    # ------------------------------------------------------------------------------------------------------------------

    # Bloco responsável por renderizar o quadrado no final do corpo da snake -------------------------------------------
    if body[-1].direction == UP:
        x = (body[-1].rect[0]) // 36
        y = (body[-1].rect[1] + 30) // 36
    elif body[-1].direction == DOWN:
        x = (body[-1].rect[0]) // 36
        y = (body[-1].rect[1]) // 36
    elif body[-1].direction == LEFT:
        x = (body[-1].rect[0] + 30) // 36
        y = (body[-1].rect[1]) // 36
    else:
        x = (body[-1].rect[0]) // 36
        y = (body[-1].rect[1]) // 36

    move_square(x, y)
    # ------------------------------------------------------------------------------------------------------------------

    # Bloco responsável por movimentar a snake -------------------------------------------------------------------------
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
    # ------------------------------------------------------------------------------------------------------------------

    # Bloco responsável por fechar o jogo caso a snake bata nela mesma -------------------------------------------------
    for i in range(2, len(body)):
        if pygame.Rect.colliderect(body[0].rect, body[i].rect):
            running = False
    # ------------------------------------------------------------------------------------------------------------------

    # Bloco responsável por aumentar o tamanho da snake caso ela coma algum pontinho -----------------------------------
    if pygame.Rect.colliderect(point.rect, body[0].rect):
        x = (point.rect[0]) // 36
        y = (point.rect[1]) // 36
        move_square(x, y)
        screen.blit(body[0].body, body[0].rect)

        point.rect.update(randint(0, 22) * 36 + 3, randint(0, 17) * 36 + 3, 30, 30)
        i = 0
        while i < len(body):
            if pygame.Rect.colliderect(point.rect, body[i].rect):
                point.rect.update(randint(0, 23) * 36 + 3, randint(0, 17) * 36 + 3, 30, 30)
                i = 0
            else:
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
        screen.blit(point.body, point.rect)
    # ------------------------------------------------------------------------------------------------------------------

    # Bloco responsável por telestransportar a snake caso ela saia do cenario ------------------------------------------
    for i in range(len(body)):
        if body[i].rect[0] > 797 and body[i].direction == RIGHT:
            corners.append(Corner())
            corners[-1].rect.update(body[i].rect[0], body[i].rect[1], 30, 30)
            body[i].rect.update(-30, body[i].rect[1], 30, 30)
        elif body[i].rect[0] < 0 and body[i].direction == LEFT:
            corners.append(Corner())
            corners[-1].rect.update(body[i].rect[0], body[i].rect[1], 30, 30)
            body[i].rect.update(861, body[i].rect[1], 30, 30)
        elif body[i].rect[1] > 647 and body[i].direction == DOWN:
            corners.append(Corner())
            corners[-1].rect.update(body[i].rect[0], body[i].rect[1], 30, 30)
            body[i].rect.update(body[i].rect[0], -35, 30, 30)
        elif body[i].rect[1] < 0 and body[i].direction == UP:
            corners.append(Corner())
            corners[-1].rect.update(body[i].rect[0], body[i].rect[1], 30, 30)
            body[i].rect.update(body[i].rect[0], 681, 30, 30)
    # ------------------------------------------------------------------------------------------------------------------

    load_snake()

    # Bloco responsável por apagar os corners que não são mais necesaários e renderizar os outros ----------------------
    if len(corners) != 0:
        for i in range(len(corners)):
            corners[i].colliding = False

        i = 0
        while i < len(body) - 1:
            j = 0
            while j < len(corners):
                if pygame.Rect.colliderect(body[i].rect, corners[j].rect):
                    corners[j].colliding = True
                    break
                j = j + 1
            i = i + 1

        i = 0
        while i < len(corners):
            if not corners[i].colliding:
                del corners[i]
            else:
                i = i + 1

        for i in range(len(corners)):
            screen.blit(corners[i].body, corners[i].rect)
    # ------------------------------------------------------------------------------------------------------------------

    # Atualiza a tela
    pygame.display.flip()

    # Max fps
    clock.tick(67 + len(body))

screen.blit(gameOver, (274, 212))
pygame.display.flip()
sleep(4)

pygame.quit()

print("Fim")
