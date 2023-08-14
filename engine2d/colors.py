class Colors:

    colors_dict = {
        "white": (255, 255, 255),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "red": (255, 0, 0),
        "aqua": (0, 255, 255),
        "magenta": (255, 0, 255)
    }

    current_color = colors_dict["white"]

    def change_color(self, new_color):
        if new_color in Colors.colors_dict.keys():
            self.current_color = Colors.colors_dict[new_color]
        else:
            print(
                f"Color {new_color} doesn't contain in Color dictionary, use one of these colors {Colors.colors_dict.keys()}")
