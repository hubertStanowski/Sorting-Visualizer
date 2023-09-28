import pygame
import random

WINDOW_WIDTH, WINDOW_HEIGHT = 1500, 950
TOP_BAR = 250
BOTTOM_BAR = 50
SIDE_BAR = 50
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
FONT = None

buttons = []
max_value = None
animation_speed = "F"
size = "M"
delay = 0

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

SELECTION_COLOR = (186, 85, 211)


pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualizer")


def main():
    global buttons, max_value, animation_speed, size, delay
    selected_algorithm = None

    algo_buttons = [Button(50, 30, text="Selection Sort", algorithm=selection_sort),
                    Button(100+BUTTON_WIDTH, 30, text="Insertion Sort",
                           algorithm=insertion_sort),
                    Button(150+2*BUTTON_WIDTH, 30,
                           text="Merge Sort", text_offset=16, algorithm=merge_sort),
                    Button(200+3*BUTTON_WIDTH, 30, text="Quick Sort", text_offset=17, algorithm=quick_sort)]

    control_buttons = [Button(400 + 6*BUTTON_WIDTH, 30, text="RUN",
                              color=GREEN, text_offset=32, height_offset=15, font_size=50),
                       Button(350 + 5*BUTTON_WIDTH, 30, text="SHUFFLE",
                              color=YELLOW, text_offset=5, height_offset=6, font_size=40)]

    speed_buttons = [SmallButton("S", 400+3*BUTTON_WIDTH-20, 40),
                     SmallButton("N", 435+3*BUTTON_WIDTH-20, 40),
                     SmallButton("F", 470+3*BUTTON_WIDTH-20, 40)]
    size_buttons = [SmallButton("S", 400+4*BUTTON_WIDTH-30, 40),
                    SmallButton("M", 435+4*BUTTON_WIDTH-30, 40, offset=-2),
                    SmallButton("L", 470+4*BUTTON_WIDTH-30, 40)]

    buttons += algo_buttons+control_buttons+speed_buttons+size_buttons

    if animation_speed == "S":
        speed_buttons[0].color = SELECTION_COLOR
        delay = 40
    elif animation_speed == "N":
        speed_buttons[1].color = SELECTION_COLOR
        delay = 15
    elif animation_speed == "F":
        speed_buttons[2].color = SELECTION_COLOR
        delay = 0

    if size == "S":
        size_buttons[0].color = SELECTION_COLOR
        array_size = 50
    elif size == "M":
        size_buttons[1].color = SELECTION_COLOR
        array_size = 100
    elif size == "L":
        size_buttons[2].color = SELECTION_COLOR
        array_size = 200

    array = [i for i in range(1, array_size + 1)]
    max_value = max(array)
    random.shuffle(array)
    visual_array = generate_visual_array(array)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                for button in algo_buttons:
                    if button.rect.collidepoint(pos):
                        selected_algorithm = button.algorithm
                        button.color = SELECTION_COLOR
                        for other in algo_buttons:
                            if other is not button:
                                other.color = WHITE
                for button in control_buttons:
                    if button.rect.collidepoint(pos):
                        if button.text == "RUN" and selected_algorithm is not None:
                            visual_array = generate_visual_array(selected_algorithm(
                                array, visual_array))

                            final_scan(visual_array)
                        elif button.text == "SHUFFLE":
                            random.shuffle(array)
                            visual_array = generate_visual_array(array)
                for button in speed_buttons:
                    if button.rect.collidepoint(pos):
                        button.color = SELECTION_COLOR
                        speed = button.text
                        for other in speed_buttons:
                            if other is not button:
                                other.color = WHITE
                        if speed == "S":
                            delay = 40
                        elif speed == "N":
                            delay = 15
                        elif speed == "F":
                            delay = 0

                for button in size_buttons:
                    if button.rect.collidepoint(pos):
                        button.color = SELECTION_COLOR
                        size = button.text
                        for other in size_buttons:
                            if other is not button:
                                other.color = WHITE
                        if size == "S":
                            array_size = 50
                        elif size == "M":
                            array_size = 100
                        elif size == "L":
                            array_size = 200

                        array = [i for i in range(1, array_size + 1)]
                        max_value = max(array)
                        random.shuffle(array)
                        visual_array = generate_visual_array(array)

        draw(visual_array)


def generate_visual_array(array):
    stripe_width = (WINDOW_WIDTH - SIDE_BAR*2) // len(array)
    visual_array = [x for x in range(len(array))]
    for i in range(len(array)):
        stripe_height = round(
            array[i] / max_value * (WINDOW_HEIGHT-TOP_BAR-BOTTOM_BAR))
        visual_array[i] = ArrayNode(
            color=WHITE,
            x=stripe_width * i + SIDE_BAR,
            y=WINDOW_HEIGHT - stripe_height - BOTTOM_BAR,
            width=stripe_width,
            height=stripe_height
        )
    return visual_array


def draw(visual_array):
    WINDOW.fill(BLACK)
    draw_legend()

    for node in visual_array:
        node.draw()

    for button in buttons:
        button.draw()

    pygame.display.update()


def draw_legend():
    draw_legend_node("Speed", 400+3*BUTTON_WIDTH-4, 7)
    draw_legend_node("Size", 400+4*BUTTON_WIDTH-4, 7)


def draw_legend_node(text, x, y):
    font = pygame.font.SysFont(FONT, 32)
    label = font.render(text, True, WHITE)

    text_rect = pygame.Rect(x, y, 100, 50)
    WINDOW.blit(label, text_rect)


def final_scan(visual_array):
    pygame.time.delay(10)
    for node in visual_array:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        node.color = GREEN
        draw(visual_array)
        pygame.time.delay(delay)

    pygame.time.delay(80)
    for node in visual_array:
        node.color = WHITE
    draw(visual_array)


# *** Algorithms ***


def selection_sort(array, visual_array):
    for i in range(len(array)):
        min_idx = find_min_idx(array, visual_array, i)
        array = swap(i, min_idx, array)
        visual_array = generate_visual_array(array)
        visual_array[i].color = GREEN
        draw(visual_array)

    return array


def find_min_idx(array, visual_array, start_idx):
    global delay
    min_idx = start_idx

    for i in range(start_idx+1, len(array)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        visual_array[i].color = BLUE

        if array[i] < array[min_idx]:
            visual_array[min_idx].color = WHITE
            min_idx = i

        draw(visual_array)
        pygame.time.delay(delay)
        visual_array[min_idx].color = RED
        visual_array[i].color = WHITE

    return min_idx


# Swaps two values in an array by indexes and returns an updated array
def swap(idx_1, idx_2, array):
    array[idx_1], array[idx_2] = array[idx_2], array[idx_1]

    return array


def insertion_sort(array, visual_array):
    for i in range(1, len(array)):
        visual_array = insert(i, array, visual_array)

    return visual_array


# Swaps an element with the one that proceeds it
def slide_to_left(idx, array):
    if idx > 0:
        array[idx - 1], array[idx] = array[idx], array[idx - 1]

    return array


def insert(idx, array, visual_array):
    global delay
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    current = array[idx]
    green_idx = idx
    prev_idx = idx - 1
    while prev_idx >= 0 and current < array[prev_idx]:
        array = slide_to_left(idx, array)
        visual_array = generate_visual_array(array)
        prev_idx -= 1
        idx -= 1
        visual_array[idx].color = RED
        if prev_idx >= 0:
            visual_array[prev_idx].color = BLUE
        visual_array[green_idx].color = GREEN
        pygame.time.delay(delay)

        draw(visual_array)

    return array


class ArrayNode:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(WINDOW, self.color,
                         (self.x, self.y, self.width, self.height))

        pygame.draw.rect(WINDOW, (0, 0, 0),
                         (self.x, self.y, self.width, self.height), 1)


class Button():
    def __init__(self, x, y, color=WHITE, text="", text_offset=0, height_offset=0, algorithm=None, font_size=30):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(
            x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.text = text
        self.text_offset = text_offset
        self.height_offset = height_offset
        self.algorithm = algorithm
        self.font_size = font_size

    def draw(self):
        pygame.draw.rect(WINDOW, self.color, self.rect)
        font = pygame.font.SysFont(FONT, self.font_size)
        label = font.render(self.text, True, BLACK)
        text_rect = pygame.Rect(
            self.x + 5 + self.text_offset, self.y + 16 - self.height_offset // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
        WINDOW.blit(label, text_rect)


class SmallButton:
    def __init__(self, text, x, y, offset=0, color=WHITE):
        self.text = text
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = color
        self.offset = offset

    def draw(self):
        pygame.draw.rect(WINDOW, self.color, self.rect)
        font = pygame.font.SysFont(FONT, 40)
        label = font.render(self.text, True, BLACK)
        text_rect = pygame.Rect(
            self.x+6 + self.offset, self.y + 3, 30, 30)
        WINDOW.blit(label, text_rect)


if __name__ == "__main__":
    main()
