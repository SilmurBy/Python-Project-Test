import cairo


class Rectangle:
    def __init__(self, color, x, y, w, h):
        self.color = color
        self.red = self.color[0]
        self.green = self.color[1]
        self.blue = self.color[2]
        self.a_x = x
        self.a_y = y
        self.w = w
        self.h = h
        self.text = f"Rectangle:({self.a_x}, {self.a_y}) with w:h {self.w}:{self.h} color {color}"

    def draw(self, surface):
        self.a_x += 400
        ctx = cairo.Context(surface)
        ctx.set_line_width(3)
        ctx.set_source_rgb(self.red, self.green, self.blue)
        ctx.rectangle(self.a_x, self.a_y, self.w, self.h)
        ctx.stroke()
        print(f"Drawing Rectangle:({self.a_x}, {self.a_y}) with radius w:h {self.w}:{self.h}")
