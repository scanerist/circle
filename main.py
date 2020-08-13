import sys

import pygame

from settings import setts

from snake import Snake

import game_functions as gf


def run_game():
    # инициализирует pygame, settings и объект экрана
    pygame.init()
    sg_settings = setts()
    screen =  pygame.display.set_mode(
        (sg_settings.width, sg_settings.height,))
    pygame.display.set_caption("")


    # создание змейки
    snake = Snake(sg_settings, screen)

    #запуск основного цикла игры
    while True:
        gf.check_events(snake)
        snake.update()
        gf.update_screen(sg_settings, screen, snake)
        # прорисовка экрана при каждом проходе цикла
        screen.fill(sg_settings.bg_color)
        snake.blitme()

        # отображение последнего прорисованного экрана
        pygame.display.flip()


run_game()
