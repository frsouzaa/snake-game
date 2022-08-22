import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 813  # 814 no total, a tela começa no 0
SCREEN_HEIGHT = 663  # 664 no total, a tela começa com 0
pixels = 3


class Body(pygame.sprite.Sprite):
    def __init__(self):
        super(Body, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill((80, 242, 112))
        self.rect = self.body.get_rect()
        self.direction = 1


class Curva(pygame.sprite.Sprite):
    def __init__(self):
        super(Curva, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill((254, 0, 0))
        self.rect = self.body.get_rect()
        self.rect.move_ip(10, 10)
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


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

body = [Body(), Body(), Body()]
curva = []

body[0].rect.update(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 30, 30)
body[1].rect.update(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30, 30, 30)
body[2].rect.update(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60, 30, 30)

body[0].body.fill((60, 254, 60))
body[2].body.fill((254, 254, 60))

running = True

clock = pygame.time.Clock()

lastKey = [None, None]
direction = None
pressedKey = None
x = 0

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[K_UP] and lastKey[0] != 2 and lastKey[0] != 1:
        print("up")
        body[0].direction = 1
        lastKey[0] = 1
        direction = 1
        curva.append(Curva())
        curva[-1].rect.update(body[0].rect[0], body[0].rect[1], 30, 30)
        screen.blit(curva[-1].body, curva[-1].rect)
    if pressedKeys[K_DOWN] and lastKey[0] != 1 and lastKey[0] != 2:
        print("down")
        body[0].direction = 2
        lastKey[0] = 2
        direction = 2
        curva.append(Curva())
        curva[-1].rect.update(body[0].rect[0], body[0].rect[1], 30, 30)
        screen.blit(curva[-1].body, curva[-1].rect)
    if pressedKeys[K_LEFT] and lastKey[0] != 4 and lastKey[0] != 3:
        print("left")
        body[0].direction = 3
        lastKey[0] = 3
        direction = 3
        curva.append(Curva())
        curva[-1].rect.update(body[0].rect[0], body[0].rect[1], 30, 30)
        screen.blit(curva[-1].body, curva[-1].rect)
    if pressedKeys[K_RIGHT] and lastKey[0] != 3 and lastKey[0] != 4:
        print("right")
        body[0].direction = 4
        lastKey[0] = 4
        direction = 4
        curva.append(Curva())
        curva[-1].rect.update(body[0].rect[0], body[0].rect[1], 30, 30)
        screen.blit(curva[-1].body, curva[-1].rect)

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

    if body[0].rect[0] >= 781 or body[0].rect[0] <= 1 or body[0].rect[1] >= 631 or body[0].rect[1] <= 1:
        running = False

    screen.fill((1, 56, 12))

    for i in range(len(body)):
        screen.blit(body[i].body, body[i].rect)

    if len(curva) != 0:
        for i in range(len(curva)):
            curva[i].colliding = False

        i = 0
        while i < len(body):
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

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

print("Fim")
