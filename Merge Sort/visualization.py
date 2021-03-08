import pygame
import random

pygame.init()

win_width = 1300
win_height = 600

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Merge Sort")


array = [x for x in range(1, 101)]
random.shuffle(array)
m = max(array)


def merge(array, p, q, r, elements):
    end1 = q-p+1
    end2 = r-q
    half_1 = []
    half_2 = []

    for i in range(end1):
        half_1.append(array[p+i])

    for j in range(end2):
        half_2.append(array[q+1+j])

    i = 0
    j = 0
    k = p
    delay = 0
    while i < len(half_1) and j < len(half_2):
        if half_1[i] <= half_2[j]:
            array[k] = half_1[i]
            i += 1
        else:
            array[k] = half_2[j]
            j += 1
        k += 1
        elements = create_rects(array)

        elements[q+i][0] = (255, 0, 0)
        elements[p+i][0] = (255, 0, 0)
        elements[r][0] = (0, 255, 0)
        draw_window(win, elements)
        pygame.time.delay(delay)
        elements[q+i][0] = (255, 255, 255)
        elements[p+i][0] = (255, 255, 255)
        elements[r][0] = (0, 255, 0)
        draw_window(win, elements)
        elements[r][0] = (0, 255, 0)
        elements[k][0] = (0, 0, 255)
        draw_window(win, elements)
        pygame.time.delay(delay)

    while i < len(half_1):
        array[k] = half_1[i]
        i += 1
        k += 1
        elements = create_rects(array)
        draw_window(win, elements)
        pygame.time.delay(delay)

    while j < len(half_2):
        array[k] = half_2[j]
        j += 1
        k += 1
        elements = create_rects(array)
        draw_window(win, elements)
        pygame.time.delay(delay)

    return create_rects(array)


def merge_sort(array, p, r, elements):
    if p < r:
        q = (p+r-1)//2
        merge_sort(array, p, q, elements)
        merge_sort(array, q+1, r, elements)
        return merge(array, p, q, r, elements)


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


def draw_window(win, elements):
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
            elements = merge_sort(array, 0, len(array)-1, elements)
            finished = True

            final_scan(win, elements)


main(win, array)
