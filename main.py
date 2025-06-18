"""основной цикл и создание экземпляров GameModel и GameView"""
import pygame
import asyncio
import platform
import sys
from game_model import GameModel
from game_view import GameView
from constants import *

def setup_game():
    """Инициализирует игру и возвращает основные компоненты"""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ball Catcher")
    
    # Создание модели и представления
    model = GameModel()
    view = GameView(screen)
    
    return model, view, screen

async def main_loop():
    """Основной игровой цикл"""
    model, view, screen = setup_game()
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                model.save_high_score()
                running = False
              
        
        # Обработка состояния меню
        if model.state == MENU:
            start_clicked, score_clicked, exit_clicked = view.draw_menu(model.high_score)
            
            if start_clicked:
                model.reset_game()
            elif score_clicked:
                model.state = HIGH_SCORE
            elif exit_clicked:
                running = False
        
        # Обработка экрана рекордов
        elif model.state == HIGH_SCORE:
            back_clicked = view.draw_high_score(model.high_score)
            if back_clicked:
                model.state = MENU
        
        # Обработка экрана окончания игры
        elif model.state == GAME_OVER:
            menu_clicked, restart_clicked = view.draw_game_over(model.score, model.high_score)
            
            if menu_clicked:
                model.state = MENU
            elif restart_clicked:
                model.reset_game()
        
        # Обработка игрового процесса
        elif model.state == PLAYING:
            # Обработка движение корзины
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                model.basket.move("left")
            if keys[pygame.K_RIGHT]:
                model.basket.move("right")
            
            # Отрисовка игры
            view.draw_game(model.basket, model.balls, model.rocks, model.score, model.lives)
            
        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(1.0 / FPS)
    
    # Завершение работы
    model.save_high_score()
    pygame.quit()
    sys.exit()

# Запуск игры
if __name__ == "__main__":
    if platform.system() == "Emscripten":
        asyncio.ensure_future(main_loop())
    else:
        asyncio.run(main_loop())
