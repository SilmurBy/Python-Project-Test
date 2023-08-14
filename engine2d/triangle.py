import math
import cairo


def normalize(angle):
    return (angle - 90) / ((-90) - 90)


def get_third_coord(a_x, a_y, b_x, b_y, angle):
    coordinates_bool = a_x >= 0 and a_y >= 0 and b_x >= 0 and b_y >= 0 and (a_x != b_x or a_y != b_y)
    angle_bool = angle != 0 and -180 < angle < 180
    if coordinates_bool and angle_bool:
        dx = b_x - a_x
        dy = b_y - a_y
        alpha = float(angle) / 180 * math.pi
        _x = a_x + math.cos(alpha) * dx + math.sin(alpha) * dy
        _y = a_y + math.sin(-alpha) * dx + math.cos(alpha) * dy
        return _x, _y
    else:
        print(f"Triangle data wrong format: expected a_x, a_y, b_x, b_y > 0, angle not 0 and -90 <= angle <= 90")
        return False, False


class Triangle:
    def __init__(self, color, a_x, a_y, b_x, b_y, angle):
        self.color = color
        self.red = self.color[0]
        self.green = self.color[1]
        self.blue = self.color[2]
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x, self.c_y = get_third_coord(a_x, a_y, b_x, b_y, angle)
        self.angle = angle
        self.text = f"Triangle:({self.a_x};{self.a_y}, {self.b_x};{self.b_y}, {self.c_x};{self.c_y}) color {color}"

    def draw(self, surface):
        if type(self.c_x) == int or type(self.c_x) == float:
            self.a_x += 400
            self.b_x += 400
            self.c_x += 400
            ctx = cairo.Context(surface)
            ctx.set_line_width(3)
            ctx.set_source_rgb(self.red, self.green, self.blue)
            ctx.move_to(self.a_x, self.a_y)
            ctx.line_to(self.b_x, self.b_y)
            ctx.line_to(self.c_x, self.c_y)
            ctx.close_path()
            ctx.stroke()
            print(f"Drawing Triangle:({self.a_x};{self.a_y}, {self.b_x};{self.b_y}, {self.c_x};{self.c_y})")
