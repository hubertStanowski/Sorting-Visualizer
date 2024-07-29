def save_settings(screen):
    with open("settings.txt", "w") as file:
        file.write(f"{screen.array.size} ")
        file.write(f"{screen.animation_speed}")
