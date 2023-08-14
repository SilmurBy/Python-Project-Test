import math
import cairo


class Circle:

    def __init__(self, color, x, y, radius):
        self.color = color
        self.red = self.color[0]
        self.green = self.color[1]
        self.blue = self.color[2]
        self.a_x = x
        self.a_y = y
        self.radius = radius
        self.text = f"Circle:({self.a_x}, {self.a_y}) with radius {self.radius} color {color}"

    def draw(self, surface):
        self.a_x += 400
        ctx = cairo.Context(surface)
        ctx.set_line_width(3)
        ctx.set_source_rgb(self.red, self.green, self.blue)
        ctx.arc(self.a_x, self.a_y, self.radius, 0, 2.0 * math.pi)
        ctx.stroke()
        print(f"Drawing Circle:({self.a_x}, {self.a_y}) with radius {self.radius}")
