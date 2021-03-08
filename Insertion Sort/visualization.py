import pygame
import random

pygame.init()

win_width = 1300
win_height = 600

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Insertion Sort")

array = [x for x in range(1, 101)]
random.shuffle(array)


def slide_to_left(idx, array, elements):
    if idx > 0:
        array[idx-1], array[idx] = array[idx], array[idx-1]

    return array


def insert(idx, array, elements):
    delay = 0
    current = array[idx]
    green_idx = idx
    prev_idx = idx-1
    while prev_idx >= 0 and current < array[prev_idx]:

        pygame.time.delay(delay)
        array = slide_to_left(idx, array, elements)
        elements = create_rects(array)
        prev_idx -= 1
        idx -= 1
        elements[idx][0] = (255, 0, 0)
        pygame.time.delay(delay)
        if prev_idx >= 0:
            elements[prev_idx][0] = (0, 0, 255)
        pygame.time.delay(delay)
        elements[green_idx][0] = (0, 255, 0)
        pygame.time.delay(delay)

        draw_window(win, elements)

    return [array, elements]


def sort(array, elements):
    for i in range(1, len(array)):
        elements = insert(i, array, elements)[1]

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


def draw_window(surface, elements):
    win.fill((0, 0, 0))
    draw_rects(elements)


def final_scan(surface, elements):
    for key in elements.keys():
        elements[key][0] = (255, 255, 255)
    draw_window(surface, elements)

    pygame.time.delay(200)

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
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not finished:
            elements = sort(array, elements)[1]
            finished = True
            final_scan(win, elements)


main(win, array)
