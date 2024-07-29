from constants import *

from random import shuffle
import pygame


class ArrayWrapper:
    def __init__(self, array_size) -> None:
        self.array = [i for i in range(1, array_size + 1)]
        shuffle(self.array)

    def draw(self, screen):
        visual_array = self.generate_visual_array()
        for node in visual_array:
            node.draw(screen)

    def generate_visual_array(self):
        stripe_width = (WINDOW_WIDTH - SIDE_BAR*2) // len(self.array)
        visual_array = self.array.copy()
        for i in range(len(self.array)):
            stripe_height = round(
                self.array[i] / len(self.array) * (WINDOW_HEIGHT-TOP_BAR-BOTTOM_BAR))
            visual_array[i] = ArrayNode(
                x=stripe_width * i + SIDE_BAR,
                y=WINDOW_HEIGHT - stripe_height - BOTTOM_BAR,
                width=stripe_width,
                height=stripe_height,
                color=WHITE,
            )
        return visual_array


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
