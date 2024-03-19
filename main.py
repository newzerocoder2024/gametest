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
    pass

pygame.quit()