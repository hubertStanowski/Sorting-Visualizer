from constants import *
from helpers import *

import pygame


class Legend:
    def __init__(self) -> None:
        self.nodes = []

    def draw(self, window):
        for node in self.nodes:
            node.draw(window)

    def add_node(self, node):
        self.nodes.append(node)


class LegendNode:
    def __init__(self, label, x, y) -> None:
        self.label = label
        self.x = x
        self.y = y

    def draw(self, window):
        font = pygame.font.SysFont(FONT, get_legend_font_size(window))

        label = font.render(self.label, True, LEGEND_FONT_COLOR)
        label_rect = label.get_rect(center=(self.x, self.y))
        window.blit(label, label_rect)


def initialize_legend(screen):
    legend = Legend()

    small_button_size = get_small_button_size(screen.window)
    animation_speed_x = screen.buttons["animation_buttons"][NORMAL].x
    size_x = screen.buttons["size_buttons"][MEDIUM].x

    x = animation_speed_x + small_button_size / 2
    y = small_button_size
    legend.add_node(LegendNode("Animation Speed", x, y))
    x = size_x + small_button_size / 2
    legend.add_node(LegendNode("Array Size", x, y))

    screen.update_legend(legend)
