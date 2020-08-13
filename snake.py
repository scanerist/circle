import pygame

import random


class Snake:

    def __init__(self, sg_settings, screen):
        """инициализация snake и его начальная позиция"""
        self.sg_settings = sg_settings
        self.screen = screen

        # загрузка изображения и получение прямоугольника
        self.image = pygame.image.load("images/snake.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image.copy()

        # появление змейки в случайном месте экрана
        self.rect.centerx = random.randint(10, 1200)
        self.rect.centery = random.randint(10, 800)
        self.center = float(self.rect.centerx)
        # флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """обновляет позицию корабля с учетом флага"""
        # обновляется атрибут center, а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.sg_settings.snake_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.sg_settings.snake_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.sg_settings.snake_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.sg_settings.snake_speed


    def blitme(self):
        """рисует змейку в текущей позиции"""
        self.screen.blit(self.image, self.rect)
