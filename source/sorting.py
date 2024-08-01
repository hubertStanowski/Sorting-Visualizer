from constants import *
from helpers import run_checks


def selection_sort(screen):
    array = screen.array
    for i in range(array.size):
        run_checks(screen)

        min_idx = find_min_idx(screen, i)
        swap(screen, i, min_idx)

        if screen.animate:
            array.values[min_idx].reset()
            array.values[i].set_color(CURRENT_COLOR)
            if i > 0:
                array.values[i-1].reset()

            array.draw(screen)

    array.values[-1].reset()


def find_min_idx(screen, start_idx):
    array = screen.array
    min_idx = start_idx

    for i in range(start_idx+1, array.size):
        run_checks(screen)
        if screen.animate:
            array.values[i].set_color(SCAN_COLOR)
            array.values[min_idx].set_color(MIN_COLOR)
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

    prev_idx = current_idx - 1
    while prev_idx >= 0 and current < array.values[prev_idx]:
        run_checks(screen)

        swap(screen, current_idx, prev_idx)

        if screen.animate:
            array.values[start_idx].set_color(GREEN)
            array.values[current_idx].set_color(RED)
            array.values[prev_idx].set_color(BLUE)
            array.draw(screen)
            array.values[current_idx].reset()
            array.values[prev_idx].reset()

        prev_idx -= 1
        current_idx -= 1


def merge_sort(screen, start, end):
    if start >= end:
        return

    mid = (end+start-1) // 2

    merge_sort(screen, start, mid)
    merge_sort(screen, mid+1, end)
    merge(screen, start, mid, end)


def merge(screen, start, mid, end):
    array = screen.array

    left_size = mid - start + 1
    right_size = end - mid
    left = [None] * left_size
    right = [None] * right_size

    # keeping pointers to nodes resulted in color duplication even after reseting them, so storing values and resizing instead
    for left_idx in range(left_size):
        left[left_idx] = array.values[start + left_idx].value

    for right_idx in range(right_size):
        right[right_idx] = array.values[mid + 1 + right_idx].value

    left_idx = 0
    right_idx = 0
    merge_idx = start

    while left_idx < left_size and right_idx < right_size:
        run_checks(screen)

        if left[left_idx] <= right[right_idx]:
            array.values[merge_idx].value = left[left_idx]
            left_idx += 1
        else:
            array.values[merge_idx].value = right[right_idx]
            right_idx += 1
        merge_idx += 1

        if screen.animate:
            array.values[start+left_idx].set_color(RED)
            array.values[mid+right_idx].set_color(RED)
            array.values[end].set_color(GREEN)
            array.values[merge_idx].set_color(BLUE)
            array.draw(screen)
            array.reset_nodes()
        array.resize_nodes(screen.window)

    while left_idx < left_size:
        run_checks(screen)

        if screen.animate:
            array.values[start+left_idx].set_color(RED)
            array.values[end].set_color(GREEN)
            array.values[merge_idx].set_color(BLUE)
            array.draw(screen)
            array.reset_nodes()
            array.resize_nodes(screen.window)

        screen.array.values[merge_idx].value = left[left_idx]
        left_idx += 1
        merge_idx += 1

    while right_idx < right_size:
        run_checks(screen)

        if screen.animate:
            array.values[mid+right_idx].set_color(RED)
            array.values[end].set_color(GREEN)
            array.values[merge_idx].set_color(BLUE)
            if screen.animate:
                array.draw(screen)
            array.reset_nodes()
            array.resize_nodes(screen.window)

        screen.array.values[merge_idx].value = right[right_idx]
        right_idx += 1
        merge_idx += 1
