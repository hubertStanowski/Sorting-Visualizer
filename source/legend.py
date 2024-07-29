from constants import *

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
    def __init__(self, label, x, y, color=None) -> None:
        self.label = label
        self.x = x
        self.y = y
        self.color = color

    def draw(self, window):
        font = pygame.font.SysFont(FONT, 32)

        font = pygame.font.SysFont(FONT, 32)
        label = font.render(self.label, True, LEGEND_FONT_COLOR)

        text_rect = pygame.Rect(self.x, self.y, 100, 50)
        window.blit(label, text_rect)


def initialize_legend(screen):
    legend = Legend()
    legend.add_node(LegendNode("Speed", 400+3*BUTTON_WIDTH-4, 7))
    legend.add_node(LegendNode("Size", 400+4*BUTTON_WIDTH-4, 7))

    screen.update_legend(legend)
