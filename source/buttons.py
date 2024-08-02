from constants import *
from helpers import *

from math import inf
import pygame


class BigButton:
    def __init__(self, screen, x, y, color=WHITE, label="", visible=True, cooldown=0, font_multiplier=1):
        self.x = x
        self.y = y
        self.width, self.height = get_big_button_size(screen.window)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = color
        self.label = label
        self.visible = visible
        self.cooldown = cooldown
        self.last_click_time = -inf
        self.font_multiplier = font_multiplier

    def draw(self, window):
        if not self.visible:
            return
        pygame.draw.rect(window, self.color, self.rect)
        font = pygame.font.SysFont(
            FONT, round(get_big_button_font_size(window) * self.font_multiplier))
        label = font.render(self.label, True, BLACK)

        label_rect = label.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2))

        window.blit(label, label_rect)

    def clicked(self, pos):
        valid = (self.visible and self.rect.collidepoint(pos))
        if self.cooldown:
            current_time = pygame.time.get_ticks()
            valid = valid and (
                current_time-self.last_click_time) > self.cooldown
            if valid:
                self.last_click_time = current_time

        return valid

    def select(self):
        self.color = SELECTION_COLOR

    def unselect(self):
        self.color = WHITE


class SmallButton:
    def __init__(self, screen, label, x, y, color=WHITE):
        self.label = label
        self.x = x
        self.y = y
        self.size = get_small_button_size(screen.window)
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        font = pygame.font.SysFont(FONT, get_small_button_font_size(window))
        label = font.render(self.label, True, BLACK)

        label_rect = label.get_rect(
            center=(self.x + self.size // 2, self.y + self.size // 2))

        window.blit(label, label_rect)

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

    def select(self):
        self.color = SELECTION_COLOR

    def unselect(self):
        self.color = WHITE


def initialize_buttons(screen, algorithm_running=False):
    window = screen.window
    window_width, _ = window.get_size()
    side_bar = get_side_bar_size(window, screen.array)
    small_button_size = get_small_button_size(window)
    big_button_width, _ = get_big_button_size(window)

    # Initialize sorting buttons
    x, y = side_bar * 0.2, small_button_size
    diff = big_button_width + window_width * 0.01

    sorting_buttons = {"Selection Sort": BigButton(screen, x, y, label="Selection Sort"),
                       "Insertion Sort": BigButton(screen, x + diff, y, label="Insertion Sort"),
                       "? Sort": BigButton(screen, x + diff*2, y, label="? Sort"),
                       "Merge Sort": BigButton(screen, x + diff*3, y,
                                               label="Merge Sort"),
                       "Quick Sort": BigButton(screen, x + diff*4, y, label="Quick Sort")}

    screen.add_buttons("sorting_buttons", sorting_buttons)
    update_sorting_buttons(screen)

    # Initialize action buttons
    left_x = x + diff*4 + big_button_width
    x = window_width-side_bar*0.2-big_button_width

    action_buttons = {"RUN": BigButton(screen, x, y, label="RUN",
                                       color=GREEN, visible=(not algorithm_running), cooldown=DEFAULT_BUTTON_COOLDOWN, font_multiplier=1.3),
                      "FINISH": BigButton(screen, x, y, label="FINISH",
                                          color=BLUE, visible=algorithm_running, cooldown=DEFAULT_BUTTON_COOLDOWN, font_multiplier=1.3),
                      "SHUFFLE": BigButton(screen, x - diff, y, label="SHUFFLE",
                                           color=YELLOW, font_multiplier=1.3)}

    screen.add_buttons("action_buttons", action_buttons)

    # Initialize animation buttons
    right_x = x - diff - small_button_size
    y = small_button_size * 1.5

    diff = small_button_size * 1.2

    offset = ((right_x - diff*2) -
              (left_x+diff*2+small_button_size)) / 3

    animation_buttons = {SLOW: SmallButton(screen, "S", left_x + offset, y),
                         NORMAL: SmallButton(screen, "N", left_x + diff + offset, y),
                         FAST: SmallButton(screen, "F", left_x + diff*2 + offset, y)}

    screen.add_buttons("animation_buttons", animation_buttons)
    update_animation_buttons(screen)

    # Initialize array size buttons
    size_buttons = {SMALL: SmallButton(screen, "S", right_x - diff*2 - offset, y),
                    MEDIUM: SmallButton(screen, "M", right_x - diff - offset, y),
                    LARGE: SmallButton(screen, "L", right_x - offset, y)}

    screen.add_buttons("size_buttons", size_buttons)
    update_size_buttons(screen)
