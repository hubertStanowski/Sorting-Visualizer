from constants import *
from helpers import run_checks


def selection_sort(screen):
    array = screen.array
    for i in range(array.size):
        run_checks(screen)

        min_idx = find_min_idx(screen, i)
        swap(screen, i, min_idx)

        array.values[min_idx].reset()
        array.values[min_idx].draw(screen, min_idx)
        array.values[i].set_color(SORTED_COLOR)
        array.values[i].draw(screen, i)
        if i > 0:
            array.values[i-1].reset()
            array.values[i-1].draw(screen, i-1)

    array.values[-1].reset()

    return array


def find_min_idx(screen, start_idx):
    array = screen.array
    min_idx = start_idx

    for i in range(start_idx+1, array.size):
        run_checks(screen)
        array.values[i].set_color(SCAN_COLOR)
        array.values[min_idx].set_color(MIN_COLOR)
        array.values[i].draw(screen, i)
        array.values[min_idx].draw(screen, min_idx)

        if array.values[i] < array.values[min_idx]:
            array.values[min_idx].reset()
            array.values[min_idx].draw(screen, min_idx)
            min_idx = i

        array.values[i].reset()
        array.values[i].draw(screen, i)

    return min_idx


def swap(screen, i, j):
    array = screen.array
    array.values[i], array.values[j] = array.values[j], array.values[i]
