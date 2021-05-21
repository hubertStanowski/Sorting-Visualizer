import pygame
import random

# Initializing pygame
pygame.init()

# Initializing a pygame window with a caption
win_width = 1680
win_height = 720
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Merge Sort")

# Creating and shuffling an array of 100 numbers
array = [x for x in range(1, 101)]
random.shuffle(array)
m = max(array)

# Main function
def main(win, array):
    finished = False

    elements = create_elements(array)
    draw_window(elements)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        if not finished:
            elements = merge_sort(array, 0, len(array) - 1, elements)
            finished = True

            final_scan(elements)


# Creates elements to draw on the surface (visualization)
def create_elements(array):
    max_value = m
    ele_width = win_width / len(array)
    elements = [x for x in range(1, 101)]
    for i in range(len(array)):
        ele_height = round(array[i] / max_value * (win_height - 100))
        elements[i] = {
            "color": (255, 255, 255),
            "x": ele_width * i,
            "y": win_height - ele_height,
            "width": ele_width,
            "height": ele_height
        }
    return elements


# Draws elements of the array on the surface with additional 1px black border
def draw_elements(elements):
    for el in elements:
        pygame.draw.rect(win, el["color"],
                         (el["x"], el["y"], el["width"], el["height"]))
        pygame.draw.rect(win, (0, 0, 0),
                         (el["x"], el["y"], el["width"], el["height"]), 1)

    pygame.display.update()


# Draws black window and fills it with elements of an array (draw_elements())
def draw_window(elements):
    win.fill((0, 0, 0))
    draw_elements(elements)


# Changes color of every element to green with delay and then changes it to white
def final_scan(elements):
    for el in elements:
        el["color"] = (0, 255, 0)
        draw_window(elements)
        pygame.time.delay(10)

    pygame.time.delay(50)
    for el in elements:
        el["color"] = (255, 255, 255)
    draw_window(elements)

# Merges two parts of an array
def merge(array, p, q, r, elements):
    end1 = q - p + 1
    end2 = r - q
    half_1 = []
    half_2 = []

    for i in range(end1):
        half_1.append(array[p + i])

    for j in range(end2):
        half_2.append(array[q + 1 + j])

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
        elements = create_elements(array)

        elements[q + i]["color"] = (255, 0, 0)
        elements[p + i]["color"] = (255, 0, 0)
        elements[r]["color"] = (0, 255, 0)
        draw_window(elements)
        pygame.time.delay(delay)
        elements[q+i]["color"] = (255, 255, 255)
        elements[p + i]["color"] = (255, 255, 255)
        elements[r]["color"] = (0, 255, 0)
        draw_window(elements)
        elements[r]["color"] = (0, 255, 0)
        elements[k]["color"] = (0, 0, 255)
        draw_window(elements)
        pygame.time.delay(delay)

    while i < len(half_1):
        array[k] = half_1[i]
        i += 1
        k += 1
        elements = create_elements(array)
        draw_window(elements)
        pygame.time.delay(delay)

    while j < len(half_2):
        array[k] = half_2[j]
        j += 1
        k += 1
        elements = create_elements(array)
        draw_window(elements)
        pygame.time.delay(delay)

    return create_elements(array)

# Sorts an array using merge sort and visualizes it
def merge_sort(array, p, r, elements):
    if p < r:
        q = (p + r - 1) // 2
        merge_sort(array, p, q, elements)
        merge_sort(array, q + 1, r, elements)
        return merge(array, p, q, r, elements)


main(win, array)