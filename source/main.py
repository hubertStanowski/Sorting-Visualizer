from constants import *
from helpers import *
from screen import initialize_screen

import pygame


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sorting Algorithms Visualizer")

    screen = initialize_screen(window)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_settings(screen)
                return

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

        screen.draw()


if __name__ == "__main__":
    main()
