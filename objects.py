"""Классы игровых объектов"""
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
        self.speed = 7
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.color = WHITE

    def move(self, direction):
        """Движение корзины влево/вправо"""
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WIDTH - self.w:
            self.x += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """Отрисовка корзины"""
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)

class Ball:
    """Класс полезного шарика"""
    def __init__(self):
        self.x = random.randint(BALL_R, WIDTH - BALL_R)
        self.y = -BALL_R
        self.r = 1  # Начинаем с маленького размера для анимации
        self.target_r = BALL_R
        self.color = random.choice([RED, BLUE, GREEN])
        self.speed = BALL_SPEED
        self.rect = pygame.Rect(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2)
        self.grow_speed = 0.5  # Скорость роста при появлении

    def move(self):
        """Движение шарика вниз и анимация появления"""
        self.y += self.speed
        
        # Анимация роста
        if self.r < self.target_r:
            self.r += self.grow_speed
            if self.r > self.target_r:
                self.r = self.target_r
                
        self.rect = pygame.Rect(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2)

    def draw(self, screen):
        """Отрисовка шарика"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.r))

class Rock:
    """Класс препятствия (камня)"""
    def __init__(self):
        self.x = random.randint(ROCK_R, WIDTH - ROCK_R)
        self.y = -ROCK_R
        self.r = 1  # Начинаем с маленького размера для анимации
        self.target_r = ROCK_R
        self.color = GRAY
        self.speed = ROCK_SPEED
        self.rect = pygame.Rect(self.x - self.r, self.y - self.r, self.r*2, self.r*2)
        self.grow_speed = 0.7  # Скорость роста при появлении

    def move(self):
        """Движение камня вниз и анимация появления"""
        self.y += self.speed
        
        # Анимация роста
        if self.r < self.target_r:
            self.r += self.grow_speed
            if self.r > self.target_r:
                self.r = self.target_r
                
        self.rect = pygame.Rect(self.x - self.r, self.y - self.r, self.r*2, self.r*2)

    def draw(self, screen):
        """Отрисовка камня"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.r))
