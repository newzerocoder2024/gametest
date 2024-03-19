import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Название и иконка
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load('target.png')  # Укажите свой путь к иконке, если есть
pygame.display.set_icon(icon)

# Цель
target_img = pygame.image.load('target.png')  # Укажите свой путь к спрайту цели
target_width = 50
target_height = 50
target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)

# Цвета
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


running = True
while running:
    screen.fill((0, 0, 0))  # Заливаем экран черным цветом

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка события клика мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверяем, попал ли клик по цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)

    # Рисуем цель
    screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

pygame.quit()