from constants import *
from helpers import *

from random import shuffle
import pygame


class ArrayWrapper:
    def __init__(self, array_size) -> None:
        self.values = [i for i in range(1, array_size + 1)]
        self.size = array_size
        self.shuffle()

    def draw(self, screen):
        visual_array = self.generate_visual_array(screen.window)
        for node in visual_array:
            node.draw(screen)

    def generate_visual_array(self, window):
        array_width, array_height = get_array_size(window, self)
        bottom_bar = get_bottom_bar_size(window)
        side_bar = get_side_bar_size(window, self)
        _, window_height = window.get_size()

        stripe_width = (array_width) // self.size
        visual_array = self.values.copy()
        for i in range(self.size):
            stripe_height = round(self.values[i] / self.size * (array_height))
            visual_array[i] = ArrayNode(
                x=stripe_width * i + side_bar,
                y=window_height - stripe_height - bottom_bar,
                width=stripe_width,
                height=stripe_height,
                color=WHITE
            )
        return visual_array

    def shuffle(self):
        shuffle(self.values)

# WINDOW_WIDTH, WINDOW_HEIGHT = 1500, 1000
# TOP_BAR = 250
# BOTTOM_BAR = 50
# SIDE_BAR = 50
# BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50


class ArrayNode:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen.window, self.color,
                         (self.x, self.y, self.width, self.height))

        pygame.draw.rect(screen.window, (0, 0, 0),
                         (self.x, self.y, self.width, self.height), 1)
