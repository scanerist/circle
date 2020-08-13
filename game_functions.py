import sys

import pygame


def check_keydown_events(event, snake):
        #проверка на нажатие клавиш
    if event.key == pygame.K_d:
        # вправо
        snake.moving_right = True
    if event.key == pygame.K_a:
        # влево
        snake.moving_left = True
        # вверх
    if event.key == pygame.K_w:
        snake.moving_up = True
        # вниз
    if event.key == pygame.K_s:
        snake.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, snake):
    # проверка на отпускание клавиш
    if event.key == pygame.K_d:
        snake.moving_right = False
    if event.key == pygame.K_a:
        snake.moving_left = False
    if event.key == pygame.K_w:
        snake.moving_up = False
    if event.key == pygame.K_s:
        snake.moving_down = False


def check_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, snake)


def update_screen(sg_settings, screen, snake):
    """обновление изображения на экране"""
    # прорисовка экрана
    screen.fill(sg_settings.bg_color)
    snake.blitme()

    # отображение последнего прорисованного экрана
    pygame.display.flip()
