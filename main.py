import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set up display
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Multi-Armed Hypnotic Spiral")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

running = True
num_arms = 16  # Number of arms
angles = [2 * math.pi * i / num_arms for i in range(num_arms)]
angle_increment = 0.02
distance_increment = 0.05

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    for i in range(100):
        for angle in angles:
            radius = i * 5
            x = math.cos(angle + i * angle_increment) * radius + screen_size[0] / 2
            y = math.sin(angle + i * angle_increment) * radius + screen_size[1] / 2
            pygame.draw.circle(screen, white, (int(x), int(y)), 5)

    for i in range(len(angles)):
        angles[i] += angle_increment  # Rotate each arm

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
