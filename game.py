import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("skibidi 8==D")
img_icon = pygame.image.load("d:/PyGame Folder/Image/Screenshot 2025-06-28 205311.png")
pygame.display.set_icon(img_icon)

running = True
while running:
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    pygame.draw.circle(screen, (r, g, b), (random.randint(0, 800), random.randint(0, 600)), random.randint(1, 100))
    for event in pygame.event.get():
        if (event.type==pygame.QUIT): running = False
    pygame.display.update()

pygame.quit()