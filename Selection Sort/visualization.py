import pygame
import random

# Initializing pygame
pygame.init()

# Initializing a pygame window with a caption
win_width = 1680
win_height = 720
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Selection sort")

# Creating and shuffling an array of 100 numbers
array = [i for i in range(1, 101)]
random.shuffle(array)


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
            elements = selection_sort(array, elements)
            finished = True
            final_scan(elements)


# Creates elements to draw on the surface (visualization)
def create_elements(array):
    max_value = max(array)
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


# Finds index of the smallest number in an array
def find_min_idx(start_idx, array, elements):
    min_idx = start_idx

    for i in range(start_idx + 1, len(array)):
        # Set color of the current element to blue (visualization)
        elements[i]["color"] = (0, 0, 255)

        if array[min_idx] > array[i]:
            # If min_idx changes then change previous min_idx's color to white (visualization)
            elements[min_idx]["color"] = (255, 255, 255)
            min_idx = i

        # Update the window
        draw_window(elements)
        # Set color of the current min_idx to red
        elements[min_idx]["color"] = (255, 0, 0)

        # Change color of the current element back to white
        elements[i]["color"] = (255, 255, 255)

    return min_idx


# Sorts an array using selection sort and visualizes it
def selection_sort(array, elements):
    for i in range(len(array)):
        min_idx = find_min_idx(i, array, elements)
        array = swap(i, min_idx, array)
        elements = create_elements(array)

        # Set color of ending of the sorted part to green
        elements[i]["color"] = (0, 255, 0)
        draw_window(elements)

    # Change the last element to white (it would stay colored because it is the last one)
    elements[-1]["color"] = (255, 255, 255)

    return elements


# Swaps two values in an array by indexes and returns an updated array
def swap(idx_1, idx_2, array):
    array[idx_1], array[idx_2] = array[idx_2], array[idx_1]

    return array


main(array)
