from constants import *
from helpers import *

import pygame


class Button():
    def __init__(self, x, y, color=WHITE, label=""):
        self.x = x
        self.y = y
        self.width = BUTTON_WIDTH
        self.height = BUTTON_HEIGHT
        self.color = color
        self.rect = pygame.Rect(
            x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.text = label

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        font = pygame.font.SysFont(FONT, 30)
        label = font.render(self.text, True, BLACK)

        label_rect = label.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2))

        window.blit(label, label_rect)

    def select(self):
        self.color = SELECTION_COLOR

    def unselect(self):
        self.color = WHITE


class SmallButton:
    def __init__(self, text, x, y, color=WHITE):
        self.text = text
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        font = pygame.font.SysFont(FONT, 30)
        label = font.render(self.text, True, BLACK)

        label_rect = label.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2))

        window.blit(label, label_rect)

    def select(self):
        self.color = SELECTION_COLOR

    def unselect(self):
        self.color = WHITE


def initialize_buttons(screen):
    sorting_buttons = {"Selection Sort": Button(50, 30, label="Selection Sort"),
                       "Insertion Sort": Button(100+BUTTON_WIDTH, 30, label="Insertion Sort"),
                       "Merge Sort": Button(150+2*BUTTON_WIDTH, 30,
                                            label="Merge Sort"),
                       "Quick Sort": Button(200+3*BUTTON_WIDTH, 30, label="Quick Sort")}

    screen.add_buttons("sorting_buttons", sorting_buttons)

    action_buttons = {"RUN": Button(400 + 6*BUTTON_WIDTH, 30, label="RUN",
                                    color=GREEN),
                      "SHUFFLE": Button(350 + 5*BUTTON_WIDTH, 30, label="SHUFFLE",
                                        color=YELLOW)}

    screen.add_buttons("action_buttons", action_buttons)

    animation_buttons = {SLOW: SmallButton("S", 400+3*BUTTON_WIDTH-20, 40),
                         NORMAL: SmallButton("N", 435+3*BUTTON_WIDTH-20, 40),
                         FAST: SmallButton("F", 470+3*BUTTON_WIDTH-20, 40)}

    screen.add_buttons("animation_buttons", animation_buttons)
    update_animation_buttons(screen)

    size_buttons = {SMALL: SmallButton("S", 400+4*BUTTON_WIDTH-30, 40),
                    MEDIUM: SmallButton("M", 435+4*BUTTON_WIDTH-30, 40),
                    LARGE: SmallButton("L", 470+4*BUTTON_WIDTH-30, 40)}

    screen.add_buttons("size_buttons", size_buttons)
    update_size_buttons(screen)
