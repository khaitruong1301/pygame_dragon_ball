import pygame
import sys
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Di chuyển hình b và tính điểm số trong Pygame")

# Tạo hình a và hình b dưới dạng Rect
a_width, a_height = 50, 50
a_x, a_y = 200, 300
a_rect = pygame.Rect(a_x, a_y, a_width, a_height)
a_color = (255, 0, 0)

b_width, b_height = 50, 50
b_x, b_y = 400, 300
b_rect = pygame.Rect(b_x, b_y, b_width, b_height)
b_color = (0, 255, 0)

# Tốc độ di chuyển của hình b
b_speed = 5

# Điểm số ban đầu
score = 0

# Hàm để di chuyển hình b vào một vị trí ngẫu nhiên
def move_b_to_random_position():
    b_rect.x = random.randint(0, screen_width - b_width)
    b_rect.y = random.randint(0, screen_height - b_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Xử lý sự kiện bàn phím
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        b_rect.x -= b_speed
    if keys[pygame.K_RIGHT]:
        b_rect.x += b_speed
    if keys[pygame.K_UP]:
        b_rect.y -= b_speed
    if keys[pygame.K_DOWN]:
        b_rect.y += b_speed

    # Kiểm tra va chạm giữa hai hình a và b
    if a_rect.colliderect(b_rect):
        # Tăng điểm số lên 1 đơn vị
        score += 1
        print("Điểm:", score)

        # Di chuyển hình b vào vị trí ngẫu nhiên
        move_b_to_random_position()

    screen.fill((255, 255, 255))  # Fill the screen with white color

    # Vẽ hình a và hình b lên màn hình
    pygame.draw.rect(screen, a_color, a_rect)
    pygame.draw.rect(screen, b_color, b_rect)

    pygame.display.update()
