import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("HandMotion - VERSÃO 1.1.0")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 64)
small = pygame.font.Font(None, 36)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 60, 30))

    title = font.render("HANDMOTION", True, (255, 255, 255))

    version = small.render(
        "VERSÃO 1.1.0",
        True,
        (150, 255, 150)
    )

    message = small.render(
        "VOCÊ FOI ATUALIZADO PELO SERVIDOR!",
        True,
        (220, 220, 220)
    )

    screen.blit(
        title,
        title.get_rect(center=(450, 220))
    )

    screen.blit(
        version,
        version.get_rect(center=(450, 300))
    )

    screen.blit(
        message,
        message.get_rect(center=(450, 360))
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
