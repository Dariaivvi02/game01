import pygame
import random
from constants import *

class Basket:
    """Класс корзины для ловли объектов"""
    def __init__(self):
        self.w = BASKET_W
        self.h = BASKET_H
        self.x = WIDTH // 2 - self.w // 2
        self.y = HEIGHT - 50
        self.speed = BASKET_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def move(self, direction):
        """Перемещает корзину в заданном направлении"""
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WIDTH - self.w:
            self.x += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """Отрисовывает корзину на экране"""
        pygame.draw.rect(screen, WHITE, self.rect, border_radius=10)


class FallingObject:
    """Базовый класс для падающих объектов"""
    def __init__(self, radius, speed, color):
        self.x = random.randint(radius, WIDTH - radius)
        self.y = -radius
        self.radius = radius
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(self.x - radius, self.y - radius, radius * 2, radius * 2)

    def move(self):
        """Перемещает объект вниз по экрану"""
        self.y += self.speed
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        """Отрисовывает объект на экране (должен быть реализован в подклассах)"""
        pass


class Ball(FallingObject):
    """Класс полезного шарика"""
    def __init__(self):
        super().__init__(BALL_R, BALL_SPEED, random.choice(BALL_COLORS))
        
    def draw(self, screen):
        """Отрисовывает шарик на экране"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Rock(FallingObject):
    """Класс камня"""
    def __init__(self):
        super().__init__(ROCK_R, ROCK_SPEED, ROCK_COLOR)
        
    def draw(self, screen):
        """Отрисовывает камень на экране"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
