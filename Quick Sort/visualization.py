import pygame
import math
import random

pygame.init()

win_width = 1300
win_height = 600

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Quick Sort")


array = [x for x in range(1, 101)]
random.shuffle(array)
m = max(array)


def partition(array, p, r, elements):
    delay = 30
    q = p
    pivot = array[r]
    elements[r][0] = (0, 255, 0)

    for j in range(p, r):

        if array[j] <= pivot:
            array[q], array[j] = array[j], array[q]
            q += 1

        elements = create_rects(array)
        if q >= 0:
            elements[q][0] = (255, 0, 0)
        elements[r][0] = (0, 255, 0)
        draw_window(win, elements)
        pygame.time.delay(delay)
        elements[j][0] = (0, 0, 255)
        draw_window(win, elements)
        pygame.time.delay(delay)

    array[q], array[r] = array[r], array[q]
    elements = create_rects(array)
    draw_window(win, elements)
    pygame.time.delay(delay)

    return q


def quick_sort(array, p, r, elements):
    if len(array) < 2:
        return array
    if p < r:
        q = partition(array, p, r, elements)
        quick_sort(array, p, q-1, elements)
        quick_sort(array, q+1, r, elements)
        return array


def create_rects(array):
    element_width = win_width / len(array)
    elements = {}
    for i in range(len(array)):
        height = round(array[i]/m * (win_height-100))
        elements[i] = [(255, 255, 255), element_width * (i),
                       win_height-height, element_width, height]

    return elements


def draw_rects(elements):
    for el in elements.values():
        pygame.draw.rect(win, el[0], (el[1], el[2], el[3], el[4]))
        pygame.draw.rect(win, (0, 0, 0), (el[1], el[2], el[3], el[4]), 1)
    pygame.display.update()


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
            elements = create_rects(quick_sort(
                array, 0, len(array)-1, elements))
            finished = True

            final_scan(win, elements)


main(win, array)
