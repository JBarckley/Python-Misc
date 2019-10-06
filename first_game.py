import pygame


def main():

    pygame.init()

    pygame.display.set_caption("First Game")

    screen = pygame.display.set_mode((1000, 1000))

    running = True

    while running:

        surf = pygame.Surface((100, 100))
        surf.fill((255, 255, 255))
        rect = surf.get_rect()

        screen.blit(surf, (400, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()

