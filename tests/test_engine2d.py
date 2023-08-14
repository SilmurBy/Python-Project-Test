from engine2d.circle import Circle
from engine2d.colors import Colors
from engine2d.parsers import Parsers
from engine2d.rectangle import Rectangle
from engine2d.triangle import get_third_coord, Triangle


class TestEngine2D:

    def test_triangle_third_point_positive_type(self):
        x, y = get_third_coord(145.0, 257, 45, 500, 80)
        assert (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float)

    def test_triangle_third_point_positive_value(self):
        x, y = get_third_coord(145.0, 257, 45, 500, 80)
        assert x > 0 and y > 0

    def test_triangle_third_point_same_x(self):
        x, y = get_third_coord(50, 50, 50, 100, 60)
        assert x > 0 and y > 0

    def test_triangle_third_point_same_y(self):
        x, y = get_third_coord(55, 50, 100, 50, 60)
        assert x > 0 and y > 0

    def test_triangle_third_point_zeros(self):
        x, y = get_third_coord(50, 100, 0, 0, 60)
        assert x != 0 and y != 0

    def test_triangle_third_point_minus_coord(self):
        x, y = get_third_coord(-55, 50, 100, 50, 60)
        assert not x and not y

    def test_triangle_third_point_same_coord(self):
        x, y = get_third_coord(55, 50, 55, 50, 60)
        assert not x and not y

    def test_triangle_third_point_zero_angle(self):
        x, y = get_third_coord(55, 50, 100, 50, 0)
        assert not x and not y

    def test_triangle_third_point_180_angle(self):
        x, y = get_third_coord(55, 50, 100, 50, 180)
        assert not x and not y

    def test_triangle_third_point_190_angle(self):
        x, y = get_third_coord(55, 50, 100, 50, 190)
        assert not x and not y

    def test_change_color_positive(self):
        colors = Colors()
        colors.change_color("blue")
        assert colors.current_color == (0, 0, 255)

    def test_change_color_negative_color_not_from_dict(self):
        colors = Colors()
        colors.change_color("ultramarine")
        assert colors.current_color == (255, 255, 255)

    def test_change_color_negative_not_color(self):
        colors = Colors()
        colors.change_color(45677)
        assert colors.current_color == (255, 255, 255)

    def test_parser_is_figure_positive(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert parsers.is_figure("circle", "circle")

    def test_parser_is_figure_positive_short(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert parsers.is_figure("cir", "circle")

    def test_parser_is_figure_positive_shorter(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert parsers.is_figure("c", "circle")

    def test_parser_is_figure_negative_another_letter(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.is_figure("cirkle", "circle")

    def test_parser_is_figure_negative_another_word(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.is_figure("triangle", "circle")

    def test_parser_is_figure_negative_not_word(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.is_figure("345!$%^", "circle")

    def test_parser_is_figure_negative_empty_string(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.is_figure("", "circle")

    def test_parser_triangle_parse_positive(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.triangle_parse("34, 66", "22, 44", "90")) == Triangle

    def test_parser_triangle_parse_positive_diff_separators(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.triangle_parse("34:66", "22;44", "90")) == Triangle

    def test_parser_triangle_parse_positive_diff_separators2(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.triangle_parse("34.66", "22/44", "90")) == Triangle

    def test_parser_triangle_parse_negative_not_coordinate(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("3466", "22, 44", "90")

    def test_parser_triangle_parse_negative_string(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("ffff", "22, 44", "90")

    def test_parser_triangle_parse_negative_empty_string(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("", "22, 44", "90")

    def test_parser_triangle_parse_negative_not_digit(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("f3f3553Gdd555", "22, 44", "90")

    def test_parser_triangle_parse_negative_string2(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("56,80", "ffff", "90")

    def test_parser_triangle_parse_negative_empty_string2(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("56,80", "", "90")

    def test_parser_triangle_parse_negative_not_coordinate2(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("56,80", "2244", "90")

    def test_parser_triangle_parse_negative_not_digit2(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("56,80", "f3f3553Gdd555", "90")

    def test_parser_triangle_parse_negative_input4_not_number(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("56, 80", "22, 44", "4f6")

    def test_parser_triangle_parse_negative_input4_empty(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.triangle_parse("56, 80", "22, 44", "")

    def test_parser_rectangle_parse_positive(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.rectangle_parse("34, 66", "90", "40")) == Rectangle

    def test_parser_rectangle_parse_positive_diff_separators(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.rectangle_parse("34:66", "90", "40")) == Rectangle

    def test_parser_rectangle_parse_positive_diff_separators2(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.rectangle_parse("34;66", "90", "40")) == Rectangle

    def test_parser_rectangle_parse_positive_diff_separators3(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.rectangle_parse("34.66", "90", "40")) == Rectangle

    def test_parser_rectangle_parse_negative_not_coordinate(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("3466", "90", "40")

    def test_parser_rectangle_parse_negative_string(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("ffff", "90", "40")

    def test_parser_rectangle_parse_negative_empty_string(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("", "90", "40")

    def test_parser_rectangle_parse_negative_not_digit(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("f3f3553Gdd555", "90", "40")

    def test_parser_rectangle_parse_negative_width_0(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("34, 66", "0", "40")

    def test_parser_rectangle_parse_negative_height_0(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("34, 66", "90", "0")

    def test_parser_rectangle_parse_negative_width_negative(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("34, 66", "-40", "40")

    def test_parser_rectangle_parse_negative_height_negative(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("34, 66", "90", "-90")

    def test_parser_rectangle_parse_negative_width_empty(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("34, 66", "", "40")

    def test_parser_rectangle_parse_negative_height_empty(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("34, 66", "90", "")

    def test_parser_rectangle_parse_negative_width_not_digit(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("34, 66", "First", "40")

    def test_parser_rectangle_parse_negative_height_not_digit(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.rectangle_parse("34, 66", "90", "Second")

    def test_parser_circle_parse_positive(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.circle_parse("66", "90", "200")) == Circle

    def test_parser_circle_parse_positive_zero_x_y(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert type(parsers.circle_parse("0", "0", "40")) == Circle

    def test_parser_circle_parse_negative_x_negative(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("-50", "40", "40")

    def test_parser_circle_parse_negative_y_negative(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("90", "-90", "90")

    def test_parser_circle_parse_negative_radius_negative(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("66", "90", "-90")

    def test_parser_circle_parse_negative_x_empty(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("", "100", "40")

    def test_parser_circle_parse_negative_y_empty(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("100", "", "100")

    def test_parser_circle_parse_negative_radius_empty(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("100", "40", "")

    def test_parser_circle_parse_negative_x_not_digit(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("x", "100", "40")

    def test_parser_circle_parse_negative_y_not_digit(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("66", "y", "100")

    def test_parser_circle_parse_negative_radius_not_digit(self):
        colors = Colors()
        parsers = Parsers(colors)
        assert not parsers.circle_parse("66", "100", "r")

    def test_parser_input_parsing_positive_circle(self):
        test_text = ["circle", "100", "120", "200"]
        colors = Colors()
        parsers = Parsers(colors)
        assert len(parsers.parsed_figures) == 0
        parsers.input_parsing(test_text)
        assert len(parsers.parsed_figures) == 1
        parsers.parsed_figures.clear()

    def test_parser_input_parsing_positive_rectangle(self):
        test_text = ["rectangle", "100,200", "120", "200"]
        colors = Colors()
        parsers = Parsers(colors)
        assert len(parsers.parsed_figures) == 0
        parsers.input_parsing(test_text)
        assert len(parsers.parsed_figures) == 1
        parsers.parsed_figures.clear()


    def test_parser_input_parsing_positive_triangle(self):
        test_text = ["triangle", "100,200", "300,400", "100"]
        colors = Colors()
        parsers = Parsers(colors)
        assert len(parsers.parsed_figures) == 0
        parsers.input_parsing(test_text)
        assert len(parsers.parsed_figures) == 1
        parsers.parsed_figures.clear()


    def test_parser_input_parsing_negative_figure_not_from_list(self):
        test_text = ["line", "100", "120", "200"]
        colors = Colors()
        parsers = Parsers(colors)
        assert len(parsers.parsed_figures) == 0
        parsers.input_parsing(test_text)
        assert len(parsers.parsed_figures) == 0

    def test_parser_input_parsing_negative_circle(self):
        test_text = ["circle", "100", "-120", "200"]
        colors = Colors()
        parsers = Parsers(colors)
        assert len(parsers.parsed_figures) == 0
        parsers.input_parsing(test_text)
        assert len(parsers.parsed_figures) == 0

    def test_parser_input_parsing_negative_rectangle(self):
        test_text = ["rectangle", "100,200", "-120", "200"]
        colors = Colors()
        parsers = Parsers(colors)
        assert len(parsers.parsed_figures) == 0
        parsers.input_parsing(test_text)
        assert len(parsers.parsed_figures) == 0

    def test_parser_input_parsing_negative_triangle(self):
        test_text = ["triangle", "100,200", "300,400", "0"]
        colors = Colors()
        parsers = Parsers(colors)
        assert len(parsers.parsed_figures) == 0
        parsers.input_parsing(test_text)
        assert len(parsers.parsed_figures) == 0

    def test_parser_input_parsing_negative_parsed_figures_limit(self):
        test_text = ["triangle", "100,200", "300,400", "100"]
        colors = Colors()
        parsers = Parsers(colors)
        parsers.parsed_figures = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]
        assert len(parsers.parsed_figures) == 8
        parsers.input_parsing(test_text)
        assert len(parsers.parsed_figures) == 8
        parsers.parsed_figures.clear()



