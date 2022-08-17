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
pixels = 5


class Body(pygame.sprite.Sprite):
    def __init__(self):
        super(Body, self).__init__()
        self.body = pygame.Surface((30, 30))
        self.body.fill((80, 242, 112))
        self.rect = self.body.get_rect()
        self.rect.move_ip(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

body = Body()

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
        x = body.rect[0] - ((body.rect[0]) // 30) * 30
        print("up")
        lastKey[0] = 1
        direction = 1
    if pressedKeys[K_DOWN] and lastKey[0] != 1 and lastKey[0] != 2:
        x = body.rect[0] - ((body.rect[0]) // 30) * 30
        print("down")
        lastKey[0] = 2
        direction = 2
    if pressedKeys[K_LEFT] and lastKey[0] != 4 and lastKey[0] != 3:
        x = body.rect[1] - ((body.rect[1])//30)*30
        print("left")
        lastKey[0] = 3
        direction = 3
    if pressedKeys[K_RIGHT] and lastKey[0] != 3 and lastKey[0] != 4:
        x = body.rect[1] - ((body.rect[1])//30)*30
        print("right")

        lastKey[0] = 4
        direction = 4

    if direction == 1:
        if x > 0:
            body.rect.move_ip(0, -x)
            x = 0
        else:
            body.rect.move_ip(0, -pixels)
    elif direction == 2:
        if x > 0:
            body.rect.move_ip(0, x)
            x = 0
        else:
            body.rect.move_ip(0, pixels)
    elif direction == 3:
        if x > 0:
            body.rect.move_ip(-x, 0)
            x = 0
        else:
            body.rect.move_ip(-pixels, 0)
    elif direction == 4:
        if x > 0:
            body.rect.move_ip(x, 0)
            x = 0
        else:
            body.rect.move_ip(pixels, 0)

    if body.rect[0] >= 781 or body.rect[0] <= 1 or body.rect[1] >= 631 or body.rect[1] <= 1:
        running = False

    screen.fill((1, 56, 12))
    screen.blit(body.body, body.rect)
    pygame.display.flip()

    clock.tick(40)

    #print((SCREEN_WIDTH-3)//30, ((body.rect[0]+30)//30+1)*30)

pygame.quit()

print("Fim")
