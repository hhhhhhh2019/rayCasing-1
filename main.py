import pygame
from settings import *
from rayCasting import Wall, Ray, Point
from Vector import *


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

walls = [
    Wall(Vec(0, 10), Vec(300, 10))
]

run = True

p = Point(Vec(100, 100), 90, 60)

while run:
    clock.tick(FPS)

    screen.fill(BLACK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    [w.show(screen) for w in walls]

    p.show(screen, walls)

    p.p.x, p.p.y = pygame.mouse.get_pos()

    pygame.display.flip()

exit()
