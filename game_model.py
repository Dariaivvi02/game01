"""Класс GameModel содержит логику игры: состояние, объекты, счет, обработку столкновений, спавн объектов и т.д."""
import os
import random
from objects import Basket, Ball, Rock
from constants import *

class GameModel:
    """Класс игровой логики и состояния"""
    def __init__(self):
        self.state = MENU
        self.basket = Basket()
        self.balls = []
        self.rocks = []
        self.score = 0
        self.lives = 3
        self.spawn_counter = 0
        self.high_score = self.get_high_score()
        self.paused = False

    def get_high_score(self):
        """Получает рекорд из файла"""
        try:
            if os.path.exists("highscore.txt"):
                with open("highscore.txt", "r") as f:
                    return int(f.read())
        except Exception:
            return 0
        return 0

    def save_high_score(self):
        """Сохраняет рекорд в файл"""
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

    def spawn_object(self):
        """Создает новый объект (шар или камень)"""
        if random.random() < 0.7:  # 70% вероятность появления шара
            self.balls.append(Ball())
        else:
            self.rocks.append(Rock())

    def update(self):
        """Обновляет состояние игры"""
        # Создаем новые объекты
        self.spawn_counter += 1
        if self.spawn_counter % SPAWN_TIMER == 0:
            self.spawn_object()
            self.spawn_counter = 0  # Сбрасываем счетчик

        # Обновляем позиции объектов
        for ball in self.balls:
            ball.move()
        for rock in self.rocks:
            rock.move()

        # Проверяем столкновения
        self.check_collisions()

    def check_collisions(self):
        """Проверяет столкновения объектов"""
        # Обработка шаров
        for ball in self.balls[:]:
            if self.basket.rect.colliderect(ball.rect):
                self.score += 10
                self.balls.remove(ball)
            elif ball.y > HEIGHT:
                self.balls.remove(ball)
                self.lives -= 1

        # Обработка камней
        for rock in self.rocks[:]:
            if self.basket.rect.colliderect(rock.rect):
                self.rocks.remove(rock)
                self.lives -= 1
            elif rock.y > HEIGHT:
                self.rocks.remove(rock)

        # Проверка окончания игры
        if self.lives <= 0:
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            self.state = GAME_OVER

    def reset_game(self):
        """Сбрасывает состояние для новой игры"""
        self.basket = Basket()
        self.balls = []
        self.rocks = []
        self.score = 0
        self.lives = 3
        self.spawn_counter = 0
        self.paused = False
        self.state = PLAYING
