import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Shooter Game")

icon = pygame.image.load("img/ShooterDisplay.png")
pygame.display.set_icon(icon)
start_screen_img = pygame.image.load("img/ShooterDisplay.png")
start_screen_img = pygame.transform.scale(start_screen_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

target_img = pygame.image.load("img/Target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

bg_color = random_color()

def show_start_screen():
    screen.blit(start_screen_img, (0, 0))
    font = pygame.font.SysFont("georgia", 60)
    title_text = font.render("Shooter Game", True, (255, 0, 0))
    text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(title_text, text_rect)
    pygame.display.update()

running = True
game_active = False

while running:
    if not game_active:
        show_start_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif not game_active and event.type == pygame.MOUSEBUTTONDOWN:
            game_active = True

        elif game_active and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:

                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                bg_color = random_color()

    if game_active:
        screen.fill(bg_color)
        screen.blit(target_img, (target_x, target_y))
        pygame.display.update()

pygame.quit()
