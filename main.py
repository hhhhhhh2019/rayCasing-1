import pygame
from settings import *
from rayCasting import Wall, Point
from math import radians
from Vector import *
from random import randint


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

walls = []

[walls.append(Wall(Vec(randint(0, WIDTH), randint(0, HEIGHT)), Vec(randint(0, WIDTH), randint(0, HEIGHT)))) for i in range(5)]

run = True

p = Point(Vec(100, 100), 90, 60)

while run:
    clock.tick(FPS)

    screen.fill(BLACK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    [w.show(screen) for w in walls]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        p.rotate(1)

    if keys[pygame.K_RIGHT]:
        p.rotate(-1)

    d = Vec(0, 0)

    if keys[pygame.K_w]:
        d = from_angle(radians(p.a))

    if keys[pygame.K_s]:
        d = from_angle(radians(p.a + 180))

    if keys[pygame.K_a]:
        d = from_angle(radians(p.a + 90))

    if keys[pygame.K_d]:
        d = from_angle(radians(p.a - 90))

    p.render(screen, walls)

    p.p += d

    pygame.display.flip()

exit()
