from constants import *
from helpers import *
from sorting import *

from random import shuffle
import pygame


class ArrayWrapper:
    def __init__(self, window, array_size) -> None:
        self.values = [ArrayNode(i) for i in range(1, array_size + 1)]
        self.size = array_size
        self.shuffle()
        self.resize_nodes(window)

    def draw(self, screen):
        for idx, node in enumerate(self.values):
            node.draw(screen, idx)

        if screen.animate:
            pygame.display.update()
            pygame.time.delay(DELAYS[screen.animation_speed])

    def resize_nodes(self, window):
        array_width, array_height = get_array_size(window, self)

        stripe_width = (array_width) // self.size
        for i in range(self.size):
            stripe_height = round(
                self.values[i].value / self.size * (array_height))
            self.values[i].resize(
                width=stripe_width,
                height=stripe_height
            )

    def reset_nodes(self):
        for node in self.values:
            node.reset()

    def shuffle(self):
        shuffle(self.values)
        self.reset_nodes()

    def sort(self, screen):
        self.reset_nodes()
        if screen.selected_algorithm == "Selection Sort":
            selection_sort(screen)

    def scan(self, screen):
        screen.draw()
        for i in range(self.size):
            command = run_checks(screen)
            if command == RESIZED:
                self.resize_nodes()
                screen.animate = False
                self.draw(screen)
                screen.animate = True
            self.values[i].set_color(SORTED_COLOR)
            self.values[i].draw(screen, i)
            if screen.animate:
                pygame.display.update()
                pygame.time.delay(DELAYS[screen.animation_speed])

        pygame.display.update()
        if screen.animate:
            pygame.time.delay(DELAYS[screen.animation_speed]*5)

        self.reset_nodes()


class ArrayNode:
    def __init__(self, value, color=WHITE):
        self.value = value
        self.color = color

    def draw(self, screen, idx):
        _, window_height = screen.window.get_size()
        bottom_bar = get_bottom_bar_size(screen.window)
        side_bar = get_side_bar_size(screen.window, screen.array)
        _, array_height = get_array_size(screen.window, screen.array)
        x = self.width * idx + side_bar
        y = window_height - self.height - bottom_bar
        reset_y = window_height - array_height - bottom_bar

        # reset the space for the node
        pygame.draw.rect(screen.window, BLACK,
                         (x, reset_y, self.width, array_height))

        # draw the node
        pygame.draw.rect(screen.window, self.color,
                         (x, y, self.width, self.height))

        pygame.draw.rect(screen.window, (0, 0, 0),
                         (x, y, self.width, self.height), 1)

    def resize(self, width, height):
        self.width = width
        self.height = height

    def set_color(self, new_color):
        self.color = new_color

    def reset(self):
        self.color = WHITE

    def __lt__(self, other):
        return self.value < other.value
