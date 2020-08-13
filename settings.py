import random

import pygame

class setts():
    """настройки и параметры игры"""

    def __init__(self):
        # размеры экрана width x height
        self.width = 1200  # ширина окна
        self.height = 800  # длина окна
        self.bg_color = (255, 255, 255)  # цвет поля

        # параметры змейки
        self.snake_speed = random.randint(5, 10)
    def icon(self):
       Icon = pygame.image.load('icons8.png')
       pygame.display.set_icon(Icon)
