from Vector import *
from settings import *
from math import sin, cos, pi, radians, degrees
import pygame


def map(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2


class Wall:
    def __init__(self, a: Vec, b: Vec) -> None:
        self.a = a
        self.b = b

    def show(self, sc):
        pygame.draw.line(sc, WHITE, self.a.get, self.b.get)


class Ray:
    def __init__(self, a: float) -> None:
        self.d = from_angle(radians(a))

    def show(self, sc: object, p: Vec) -> None:
        pygame.draw.line(sc, RED, p.get, (self.d * 10 + p).get)

    def rotate(self, a: float) -> None:
        self.d = from_angle(radians(a) + self.d.angle)

    def cast(self, p, w):
        x1, y1 = w.a.get
        x2, y2 = w.b.get
        x3, y3 = p.get
        x4, y4 = (self.d + p).get

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if 0 < t < 1 and u > 0:
            return Vec(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
        else:
            return None


class Point:
    def __init__(self, p: Vec, fov: int, r: int, a: float = 0) -> None:
        self.p = p
        self.rays = []

        self.r = r
        self.fov = fov
        self.a = a

        self.update_rays()

    def update_rays(self):
        self.rays = []

        [self.rays.append(Ray(i + self.a)) for i in range(int(self.fov / 2), int(-self.fov / 2), int(-self.fov / self.r))]

    def rotate(self, a):
        self.a += a
        self.update_rays()

    def show(self, sc, walls):
        scene = []

        for r in self.rays:
            record = 1000000
            closest = None

            for w in walls:
                pt = r.cast(self.p, w)

                if pt:
                    d = distance(self.p, pt)

                    if d < record:
                        record = d

                        closest = pt

            if closest:
                pygame.draw.line(sc, RED, self.p.get, closest.get)

            r.show(sc, self.p)

            scene.append(record)

        return scene

    def render(self, sc, walls):
        scene = self.show(sc, walls)

        w = WIDTH / len(scene)

        for i in scene:
            h = map(i, 0, WIDTH, HEIGHT, 20)

            if h < 0:
                h = 0

            if h > 100:
                h = 100

            print(h)

            pygame.draw.rect(sc, WHITE, pygame.Rect(scene.index(i) * w, HALF_HEIGHT - h, w, h))
