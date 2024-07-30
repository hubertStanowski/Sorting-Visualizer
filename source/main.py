from constants import *
from helpers import *
from screen import initialize_screen

import pygame


def get_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


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
                for label, button in screen.buttons["action_buttons"].items():
                    if button.clicked(pos):
                        if label == "RUN" and screen.selected_algorithm:
                            toggle_run_finish_buttons(screen)
                            # toggle_run_finish_buttons(screen)
                            # visual_array = generate_visual_array(selected_algorithm(
                            #     array, visual_array))
                            # final_scan(visual_array)
                        elif label == "SHUFFLE":
                            screen.array.shuffle()

                for label, button in screen.buttons["size_buttons"].items():
                    if button.clicked(pos):
                        screen.update_array_size(label)
                        update_size_buttons(screen)

                for label, button in screen.buttons["animation_buttons"].items():
                    if button.clicked(pos):
                        screen.update_animation_speed(label)
                        update_animation_buttons(screen)

                for label, button in screen.buttons["sorting_buttons"].items():
                    if button.clicked(pos):
                        screen.selected_algorithm = label
                        update_sorting_buttons(screen)


if __name__ == "__main__":
    main()
