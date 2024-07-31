from constants import *
from helpers import run_checks


def selection_sort(screen):
    array = screen.array
    for i in range(array.size):
        run_checks(screen)

        min_idx = find_min_idx(screen, i)
        swap(screen, i, min_idx)

        array.values[min_idx].reset()
        array.values[i].set_color(CURRENT_COLOR)
        if i > 0:
            array.values[i-1].reset()

        if screen.animate:
            array.draw(screen)

    array.values[-1].reset()


def find_min_idx(screen, start_idx):
    array = screen.array
    min_idx = start_idx

    for i in range(start_idx+1, array.size):
        run_checks(screen)

        array.values[i].set_color(SCAN_COLOR)
        array.values[min_idx].set_color(MIN_COLOR)
        if screen.animate:
            array.draw(screen)

        if array.values[i] < array.values[min_idx]:
            array.values[min_idx].reset()
            min_idx = i

        array.values[i].reset()

    return min_idx


def swap(screen, i, j):
    array = screen.array
    array.values[i], array.values[j] = array.values[j], array.values[i]


def insertion_sort(screen):
    for i in range(1, screen.array.size):
        insert(screen, i)


def insert(screen, start_idx):
    array = screen.array
    current_idx = start_idx
    current = array.values[current_idx]

    array.values[start_idx].set_color(GREEN)

    prev_idx = current_idx - 1
    while prev_idx >= 0 and current < array.values[prev_idx]:
        run_checks(screen)

        swap(screen, current_idx, prev_idx)

        array.values[current_idx].set_color(RED)
        array.values[prev_idx].set_color(BLUE)

        if screen.animate:
            array.draw(screen)

        array.values[current_idx].reset()
        array.values[prev_idx].reset()

        prev_idx -= 1
        current_idx -= 1
