import pygame
import random

# Инициализация Pygame
pygame.init()


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