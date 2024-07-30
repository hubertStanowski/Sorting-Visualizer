from constants import *


def save_settings(screen):
    with open("settings.txt", "w") as file:
        file.write(f"{screen.array.size} ")
        file.write(f"{screen.animation_speed}")


def get_updated_screen_dimensions(old_dimensions, new_dimensions):
    old_width, old_height = old_dimensions
    new_width, new_height = new_dimensions

    new_width, new_height = max(new_width, 850), max(new_height, 567)
    ratio = new_height/new_width
    delta_width = new_width - old_width
    delta_height = new_height - old_height

    if not (0.53 <= ratio <= 0.70):
        if abs(delta_width) >= abs(delta_height):
            new_height = new_width * 2/3
        else:
            new_width = 3/2 * new_height

    return new_width, new_height


def get_side_bar_size(window, array):
    window_width, _ = window.get_size()
    array_width, _ = get_array_size(window, array)

    return round((window_width - array_width) / 2)


def get_bottom_bar_size(window):
    _, window_height = window.get_size()
    return round(window_height * 0.05)


def get_top_bar_size(window):
    _, window_height = window.get_size()

    return round(0.35 * window_height)


def get_array_size(window, array):
    window_width, window_height = window.get_size()
    top_bar = get_top_bar_size(window)

    array_width = window_width * 0.95
    array_height = window_height - top_bar*0.6

    array_width //= array.size
    array_width *= array.size

    return array_width, array_height


def get_small_button_size(window):
    _, window_height = window.get_size()

    return window_height * 0.035


def get_big_button_size(window):
    small_button_size = get_small_button_size(window)
    button_width = small_button_size * 4.25
    button_height = small_button_size * 5/3

    return button_width, button_height


def get_small_button_font_size(window):
    return round(get_small_button_size(window) * 0.97)


def get_big_button_font_size(window):
    _, big_button_height = get_big_button_size(window)

    return round(0.5 * big_button_height)


def get_legend_font_size(window):
    window_width, _ = window.get_size()

    return round(window_width * 0.015)


def update_animation_buttons(screen):
    for label, button in screen.buttons["animation_buttons"].items():
        if label == screen.animation_speed:
            button.select()
        else:
            button.unselect()


def update_size_buttons(screen):
    for label, button in screen.buttons["size_buttons"].items():
        if screen.array.size == label:
            button.select()
        else:
            button.unselect()


def update_sorting_buttons(screen):
    for label, button in screen.buttons["sorting_buttons"].items():
        if label == screen.selected_algorithm:
            button.select()
        else:
            button.unselect()


def toggle_run_finish_buttons(screen):
    run, finish = screen.buttons["action_buttons"]["RUN"], screen.buttons["action_buttons"]["FINISH"]
    run.visible = not run.visible
    finish.visible = not finish.visible

    # current_time = pygame.time.get_ticks()
    # run.last_click_time = current_time
    # finish.last_click_time = current_time

    screen.draw_buttons()
