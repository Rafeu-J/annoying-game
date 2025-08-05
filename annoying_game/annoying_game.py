
import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Most Annoying Game Ever")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FONT_COLOR = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 36)

# Music
pygame.mixer.init()
try:
    pygame.mixer.music.load("annoying_music.mp3")
    pygame.mixer.music.play(-1)
except:
    print("Background music file missing.")

# Target
target_radius = 30
target_x = random.randint(target_radius, WIDTH - target_radius)
target_y = random.randint(target_radius, HEIGHT - target_radius)
target_speed = 7

# Score
score = 0
start_time = time.time()

def draw_target(x, y):
    pygame.draw.circle(screen, RED, (x, y), target_radius)

def show_text(text, x, y):
    label = font.render(text, True, FONT_COLOR)
    screen.blit(label, (x, y))

# Game loop
running = True
while running:
    screen.fill(WHITE)
    draw_target(target_x, target_y)

    elapsed_time = time.time() - start_time
    show_text(f"Score: {score}", 10, 10)
    show_text(f"Time: {int(elapsed_time)}s", 10, 40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if (mx - target_x) ** 2 + (my - target_y) ** 2 < target_radius ** 2:
                score += 1
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius, HEIGHT - target_radius)
            else:
                score = max(0, score - 1)
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius, HEIGHT - target_radius)

    # Move target randomly to annoy
    target_x += random.choice([-1, 1]) * random.randint(0, target_speed)
    target_y += random.choice([-1, 1]) * random.randint(0, target_speed)
    target_x = max(target_radius, min(WIDTH - target_radius, target_x))
    target_y = max(target_radius, min(HEIGHT - target_radius, target_y))

    pygame.display.flip()
    pygame.time.delay(300)

pygame.quit()
sys.exit()
