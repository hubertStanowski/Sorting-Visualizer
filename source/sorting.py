from constants import *
from helpers import run_checks

from random import randrange


def selection_sort(screen, start, end):
    array = screen.array
    for i in range(start, end+1):
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


def insertion_sort(screen, start, end):
    array = screen.array
    for i in range(start+1, end+1):
        current_idx = i
        while current_idx > start and array.values[current_idx] < array.values[current_idx-1]:
            run_checks(screen)

            swap(screen, current_idx, current_idx-1)

            if screen.animate:
                array.values[i].set_color(GREEN)
                array.values[current_idx].set_color(RED)
                array.values[current_idx-1].set_color(BLUE)
                array.draw(screen)
                array.values[current_idx].reset()
                array.values[current_idx-1].reset()

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
            array.draw(screen)
            array.reset_nodes()
            array.resize_nodes(screen.window)

        screen.array.values[merge_idx].value = right[right_idx]
        right_idx += 1
        merge_idx += 1


def quick_sort(screen, start, end):
    if screen.array.size < 2 or start >= end:
        return

    pivot_idx = random_partition(screen, start, end)
    quick_sort(screen, start, pivot_idx - 1)
    quick_sort(screen, pivot_idx + 1, end)


def partition(screen, start, end):
    array = screen.array
    seperator_idx = start + 1
    pivot = array.values[start].value
    for j in range(start + 1, end + 1):
        run_checks(screen)

        if screen.animate:
            array.values[seperator_idx].set_color(RED)
            array.values[start].set_color(GREEN)
            array.values[j].set_color(BLUE)
            array.draw(screen)
            array.reset_nodes()

        if array.values[j].value <= pivot:
            swap(screen, seperator_idx, j)
            seperator_idx += 1

    swap(screen, seperator_idx-1, start)

    array.draw(screen)

    return seperator_idx - 1


def random_partition(screen, start, end):
    pivot_idx = randrange(start, end)
    swap(screen, start, pivot_idx)

    return partition(screen, start, end)


def tim_sort(screen):
    array = screen.array
    min_run = get_min_run_size(array.size)

    # Sort subarrays of size min_run
    for start in range(0, array.size, min_run):
        end = min(start + min_run - 1, array.size - 1)
        insertion_sort(screen, start, end)

    # Merge those individual arrays sorted earlier using insertion_sort
    merge_size = min_run
    while merge_size < array.size:
        for start in range(0, array.size, 2 * merge_size):
            mid = min(array.size - 1, start + merge_size - 1)
            end = min((start + 2 * merge_size - 1), (array.size - 1))

            if mid < end:
                merge(screen, start, mid, end)

        merge_size *= 2


def get_min_run_size(size):
    min_merge = 32

    remainder = 0
    while size >= min_merge:
        remainder |= size & 1
        size >>= 1

    return size + remainder
