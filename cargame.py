import pygame
import random

width = 800
height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGNETA = (255, 0, 255)
ORANGE = (255, 128, 0)
GRAY = (128, 128, 128)

LIST_COLOR = [RED, GREEN, BLUE, YELLOW, CYAN, MAGNETA, ORANGE]


class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.w, self.h))

    def move(self, dx, dy, bbox):
        dx = max(bbox[0], min(self.x + dx, bbox[1] - self.width))
        dy = max(0, min(self.y + dy, bbox[2] - self.height))

        self.x = dx
        self.y = dy
