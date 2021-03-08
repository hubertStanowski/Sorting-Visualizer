import pygame
import math
import random

pygame.init()

win_width = 1300
win_height = 600

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Selection Sort")


array = [x for x in range(1, 101)]
random.shuffle(array)


def swap(idx_1, idx_2, array):
    array[idx_1], array[idx_2] = array[idx_2], array[idx_1]
    return array


def find_min_idx(start_idx, array, elements):
    min_idx = start_idx
    for i in range(start_idx+1, len(array)):
        elements[i][0] = (0, 0, 255)

        if array[min_idx] > array[i]:
            elements[min_idx][0] = (255, 255, 255)
            min_idx = i

        draw_rects(elements)
        pygame.time.delay(0)
        elements[min_idx][0] = (255, 0, 0)

        elements[i][0] = (255, 255, 255)

    return min_idx


def visual_sort(array, elements, surface):
    for i in range(len(array)):
        min_idx = find_min_idx(i, array, elements)
        array = swap(i, min_idx, array)
        elements = create_rects(array)
        elements[i][0] = (0, 255, 0)
        draw_window(surface, elements)

    elements[len(elements)-1][0] = (255, 255, 255)

    return [array, elements]


def create_rects(array):
    arr_max = max(array)
    element_width = win_width / len(array)
    elements = {}
    for i in range(len(array)):
        height = round(array[i]/arr_max * (win_height-100))
        elements[i] = [(255, 255, 255), element_width * (i),
                       win_height-height, element_width, height]

    return elements


def draw_rects(elements):
    for el in elements.values():
        pygame.draw.rect(win, el[0], (el[1], el[2], el[3], el[4]))
        pygame.draw.rect(win, (0, 0, 0), (el[1], el[2], el[3], el[4]), 1)
    pygame.display.update()

# HERE ENDED REFACTORING


def draw_window(surface, elements):
    win.fill((0, 0, 0))
    draw_rects(elements)


def final_scan(surface, elements):
    for key in elements.keys():
        elements[key][0] = (0, 255, 0)
        draw_window(surface, elements)
        pygame.time.delay(10)
    pygame.time.delay(50)
    for key in elements.keys():
        elements[key][0] = (255, 255, 255)
    draw_window(surface, elements)


def main(win, array):

    run = True
    finished = False

    elements = create_rects(array)
    draw_window(win, elements)
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not finished:
            elements = visual_sort(array, elements, win)[1]
            finished = True
            final_scan(win, elements)


main(win, array)
