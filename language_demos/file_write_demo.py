

colors = ["red", "green", "blue", "yellow"]

with open("new_colors.txt", "w") as new_colors_file:

    for color in colors:
        new_colors_file.write(color + "\n")
