import pygame
import random
WIDTH = 20
HEIGHT = 16
SQUARE = 32

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_pos = (0,0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_rect = pygame.Rect(mole_pos[0] * SQUARE, mole_pos[1] * SQUARE, SQUARE, SQUARE)
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        mole_pos = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
            screen.fill("light green")
            for row in range(HEIGHT + 1):
                pygame.draw.line(screen, (0,0,139), (0, row*SQUARE), (WIDTH*SQUARE, row * SQUARE))
            for col in range(WIDTH + 1):
                pygame.draw.line(screen, (0, 0, 139), (col * SQUARE, 0),(col * SQUARE, HEIGHT * SQUARE))


            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos[0] * SQUARE, mole_pos[1]*SQUARE)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
