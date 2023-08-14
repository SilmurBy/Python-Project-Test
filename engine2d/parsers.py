import re

from engine2d.circle import Circle
from engine2d.rectangle import Rectangle
from engine2d.triangle import Triangle


class Parsers:
    parsed_inputs = []
    parsed_figures = []

    def __init__(self, colors_object):
        self.colors = colors_object

    @staticmethod
    def is_figure(text, check_word):
        check = check_word
        result = False
        for i in range(len(text)):
            if text[i] != check[i]:
                result = False
                break
            else:
                result = True
        return result

    def input_parsing(self, texts):
        if len(self.parsed_figures) >= 8:
            print(f"Can't add more then 8 objects, draw existing for clearing objets list")
        else:
            if self.is_figure(texts[0].lower(), "circle"):
                circle = self.circle_parse(texts[1], texts[2], texts[3])
                if type(circle) == Circle:
                    self.parsed_figures.append(circle)
                else:
                    print(f"Circle from inputs incorrect: {texts}")
            if self.is_figure(texts[0].lower(), "rectangle"):
                rectangle = self.rectangle_parse(texts[1], texts[2], texts[3])
                if type(rectangle) == Rectangle:
                    self.parsed_figures.append(rectangle)
                else:
                    print(f"Rectangle from inputs incorrect: {texts}")
            if self.is_figure(texts[0].lower(), "triangle"):
                triangle = self.triangle_parse(texts[1], texts[2], texts[3])
                if type(triangle) == Triangle:
                    self.parsed_figures.append(triangle)
                else:
                    print(f"Triangle from inputs incorrect: {texts}")
            self.parsed_inputs.clear()

    def circle_parse(self, input2, input3, input4):
        result = False
        if input2.isdigit() and input3.isdigit() and input4.isdigit():
            x = int(input2)
            y = int(input3)
            radius = int(input4)
            if x >= 0 and y >= 0 and radius > 0:
                result = Circle(self.colors.current_color, x, y, radius)
        return result

    def rectangle_parse(self, input2, input3, input4):
        result = False
        coordinate = re.findall('[0-9]+', input2)
        if type(coordinate) == list and len(coordinate) == 2:
            if coordinate[0].isdigit() and coordinate[1].isdigit():
                x = int(coordinate[0])
                y = int(coordinate[1])
                if x >= 0 and y >= 0 and input3.isdigit() and input4.isdigit():
                    w = int(input3)
                    h = int(input4)
                    if w > 0 and h > 0:
                        result = Rectangle(self.colors.current_color, x, y, w, h)
        return result

    def triangle_parse(self, input2, input3, input4):
        result = False
        a_coordinate = re.findall('[0-9]+', input2)
        if type(a_coordinate) == list and len(a_coordinate) == 2:
            if a_coordinate[0].isdigit() and a_coordinate[1].isdigit():
                a_x = int(a_coordinate[0])
                a_y = int(a_coordinate[1])
                b_coordinate = re.findall('[0-9]+', input3)
                if type(b_coordinate) == list and len(b_coordinate) == 2:
                    if b_coordinate[0].isdigit() and b_coordinate[1].isdigit():
                        b_x = int(b_coordinate[0])
                        b_y = int(b_coordinate[1])
                        if input4.isdigit():
                            triangle = Triangle(self.colors.current_color, a_x, a_y, b_x, b_y, int(input4))
                            if type(triangle.c_x) == int or type(triangle.c_x) == float:
                                result = triangle
        return result
