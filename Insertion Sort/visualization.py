import pygame
import random

# Initializing pygame
pygame.init()

# Initializing a pygame widow with a caption
win_width = 1680
win_height = 720
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Insertion Sort")

# Creating and shuffling an array of 100 numbers
array = [x for x in range(1, 101)]
random.shuffle(array)
m = max(array)

# Main function
def main(array):
    run = True
    finished = False
    elements = create_elements(array)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not finished:
            elements = insertion_sort(array, elements)[1]
            finished = True
            final_scan(elements)

# Swaps an element with the one that proceeds it
def slide_to_left(idx, array, elements):
    if idx > 0:
        array[idx - 1], array[idx] = array[idx], array[idx - 1]

    return array

# Inserts an element into an array (insertion sort)
def insert(idx, array, elements):
    delay = 0
    current = array[idx]
    green_idx = idx
    prev_idx = idx - 1
    while prev_idx >= 0 and current < array[prev_idx]:

        pygame.time.delay(delay)
        array = slide_to_left(idx, array, elements)
        elements = create_elements(array)
        prev_idx -= 1
        idx -= 1
        elements[idx]["color"] = (255, 0, 0)
        pygame.time.delay(delay)
        if prev_idx >= 0:
            elements[prev_idx]["color"] = (0, 0, 255)
        pygame.time.delay(delay)
        elements[green_idx]["color"] = (0, 255, 0)
        pygame.time.delay(delay)

        draw_window(elements)

    return [array, elements]

# Sorts an array using insertion sort
def insertion_sort(array, elements):
    for i in range(1, len(array)):
        elements = insert(i, array, elements)[1]

    return [array, elements]

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
        el["color"] = (255, 255, 255)
    draw_window(elements)
    
    for el in elements:
        el["color"] = (0, 255, 0)
        draw_window(elements)
        pygame.time.delay(10)

    pygame.time.delay(50)
    for el in elements:
        el["color"] = (255, 255, 255)
    draw_window(elements)


main(array)

