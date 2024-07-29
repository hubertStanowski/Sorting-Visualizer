def save_settings(screen):
    with open("settings.txt", "w") as file:
        file.write(f"{screen.array.size} ")
        file.write(f"{screen.animation_speed}")


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
