from constants import *
from helpers import *
from screen import initialize_screen

import pygame


def main():
    pygame.init()
    window = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Sorting Algorithms Visualizer")

    screen = initialize_screen(window)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        screen.draw()
        old_width, old_height = screen.window.get_size()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_settings(screen)
                return

            if event.type == pygame.VIDEORESIZE:
                new_width, new_height = get_updated_screen_dimensions(
                    (old_width, old_height), (event.w, event.h))
                new_window = pygame.display.set_mode(
                    (new_width, new_height), pygame.RESIZABLE)
                screen.resize(new_window)

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()


if __name__ == "__main__":
    main()
