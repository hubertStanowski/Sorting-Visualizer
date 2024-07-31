from constants import *
from helpers import run_checks


def selection_sort(screen):
    array = screen.array
    for i in range(array.size):
        run_checks(screen)

        min_idx = find_min_idx(screen, i)
        swap(screen, i, min_idx)
        array.values[i].set_color(SORTED_COLOR)
        if i > 0:
            array.values[i-1].reset()
        if screen.animate:
            array.draw(screen)

    array.values[-1].reset()
    return array


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


# Swaps two values in an array by indexes and returns an updated array
def swap(screen, i, j):
    array = screen.array
    array.values[i], array.values[j] = array.values[j], array.values[i]
