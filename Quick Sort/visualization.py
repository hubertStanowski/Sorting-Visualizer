import pygame
import random

# Initializing pygame
pygame.init()

# Initializing a pygame window with a caption
win_width = 1680
win_height = 720
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Quick Sort")

# Creating and shuffling an array of 100 numbers
array = [x for x in range(1, 101)]
random.shuffle(array)
m = max(array)

# Main function
def main(array):
    finished = False

    # Seting up an array on the surface
    elements = create_elements(array)
    draw_window(elements)
    while True:

        # If exit button clicked then quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        # If not sorted then sort and end with final scan
        if not finished:
            elements = create_elements(quick_sort(array, 0, len(array) - 1, elements))
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


# Partitioning an array
def partition(array, p, r, elements):
    delay = 0
    q = p + 1
    pivot = array[p]
    elements[p]["color"] = (0, 255, 0)
    for j in range(p + 1, r + 1):

        if array[j] <= pivot:
            array[q], array[j] = array[j], array[q]
            q += 1

        elements = create_elements(array)
        if q < 100:
            elements[q]["color"] = (255, 0, 0)
        elements[p]["color"] = (0, 255, 0)
        draw_window(elements)
        pygame.time.delay(delay)
        elements[j]["color"] = (0, 0, 255)
        draw_window(elements)
        pygame.time.delay(delay)

    array[q - 1], array[p] = array[p], array[q - 1]
    elements = create_elements(array)
    draw_window(elements)
    pygame.time.delay(delay)

    return q - 1


def quick_sort(array, p, r, elements):
    if len(array) < 2:
        return array
    if p < r:
        q = random_partition(array, p, r, elements)
        quick_sort(array, p, q - 1, elements)
        quick_sort(array, q + 1, r, elements)
        return array


# Randomizing the pivot and partitioning an array
def random_partition(array, p, r, elements):
    pivot = random.randrange(p, r)
    array[p], array[pivot] = array[pivot], array[p]
    return partition(array, p, r, elements)


main(array)