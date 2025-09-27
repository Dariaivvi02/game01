"""класс GameView отвечает за отрисовку: меню, кнопок, игрового поля, HUD, экранов окончания игры и т.д."""
import pygame
from constants import *

class GameView:
    """Класс для отображения игрового состояния"""
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 36)
        self.small_font = pygame.font.SysFont("Arial", 24)

    def draw_button(self, text, x, y, width, height, normal_color, hover_color):
        """Рисует кнопку и возвращает True, если на нее нажали"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        rect = pygame.Rect(x, y, width, height)
        
        # Определяем состояние кнопки
        is_hovered = rect.collidepoint(mouse_pos)
        button_color = hover_color if is_hovered else normal_color
        
        pygame.draw.rect(self.screen, button_color, rect, border_radius=10)
        
        text_surface = self.font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)
        
        # Возвращаем True, если кнопка была нажата
        return is_hovered and mouse_clicked

    def draw_menu(self, high_score):
        """Отображает главное меню"""
        self.screen.fill(BLACK)
        
        # Заголовок
        title = self.font.render("Ball Catcher", True, YELLOW)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        
        # Кнопки
        start_clicked = self.draw_button("Start Game", WIDTH//2 - 100, 200, 200, 50, DARK_GRAY, GRAY)
        score_clicked = self.draw_button("High Score", WIDTH//2 - 100, 300, 200, 50, DARK_GRAY, GRAY)
        exit_clicked = self.draw_button("Exit", WIDTH//2 - 100, 400, 200, 50, DARK_GRAY, GRAY)
        
        return start_clicked, score_clicked, exit_clicked

    def draw_high_score(self, high_score):
        """Отображает экран с рекордом"""
        self.screen.fill(BLACK)
        
        # Отображение рекорда
        score_text = self.font.render(f"High Score: {high_score}", True, YELLOW)
        self.screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 200))
        
        # Кнопка возврата
        back_clicked = self.draw_button("Back", WIDTH//2 - 100, 400, 200, 50, DARK_GRAY, GRAY)
        return back_clicked

    def draw_game_over(self, score, high_score):
        """Отображает экран окончания игры"""
        self.screen.fill(BLACK)
        
        # Тексты
        texts = [
            self.font.render("Game Over", True, YELLOW),
            self.font.render(f"Your Score: {score}", True, WHITE),
            self.font.render(f"High Score: {high_score}", True, WHITE)
        ]
        
        # Расположение текстов
        y_pos = 150
        for text in texts:
            self.screen.blit(text, (WIDTH//2 - text.get_width()//2, y_pos))
            y_pos += 100
        
        # Кнопки
        menu_clicked = self.draw_button("Back to Menu", WIDTH//2 - 100, 450, 200, 50, DARK_GRAY, GRAY)
        restart_clicked = self.draw_button("Play Again", WIDTH//2 - 100, 520, 200, 50, DARK_GRAY, GRAY)
        
        return menu_clicked, restart_clicked

    def draw_hud(self, score, lives):
        """Отображает игровую информацию (счет и жизни)"""
        score_text = self.small_font.render(f"Score: {score}", True, WHITE)
        lives_text = self.small_font.render(f"Lives: {lives}", True, WHITE)
        
        # Отображаем в углах экрана
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

    def draw_game(self, basket, balls, rocks, score, lives):
        """Отображает игровое поле"""
        self.screen.fill(BLACK)
        
        # Рисуем объекты
        basket.draw(self.screen)
        for ball in balls:
            ball.draw(self.screen)
        for rock in rocks:
            rock.draw(self.screen)
        
        # ДОБАВЛЕНО: отображение HUD (очков и жизней)
        self.draw_hud(score, lives)

    def draw_pause(self):
        """Отображает экран паузы"""
        # Полупрозрачное затемнение
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        s.fill((0, 0, 0, 128))  # Черный с прозрачностью 50%
        self.screen.blit(s, (0, 0))
        
        # Текст паузы
        pause_text = self.font.render("PAUSED", True, YELLOW)
        self.screen.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2 - pause_text.get_height()//2))
        
        # Инструкция
        instruction = self.small_font.render("Press P to continue", True, WHITE)
        self.screen.blit(instruction, (WIDTH//2 - instruction.get_width()//2, HEIGHT//2 + 50))
