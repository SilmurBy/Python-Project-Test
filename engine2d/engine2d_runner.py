import cairo
import pygame
from time import sleep
from pygame import freetype
from button import Button
from colors import Colors
from engine2d.parsers import Parsers
from input import InputBox


class Engine2D:
    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    cairo_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.display.set_caption("Engine2D for simple geometry")
    clock = pygame.time.Clock()
    GAME_FONT = freetype.SysFont("20", 20)
    colors = Colors()
    parsers = Parsers(colors)

    draw_all_button = Button(screen, "Draw all", (20, 650), 30, "azure4")
    catch_button = Button(screen, "Catch values", (150, 650), 30, "azure4")
    change_color_button = Button(screen, "Change color", (20, 600), 30, "azure4")

    input_box1 = InputBox(400, 650, 150, 32, "Figure type")
    input_box2 = InputBox(600, 650, 150, 32, "First param")
    input_box3 = InputBox(800, 650, 150, 32, "Second param")
    input_box4 = InputBox(1000, 650, 150, 32, "Third param")
    color_input_box = InputBox(200, 600, 150, 32, "Colors")

    button_boxes = [draw_all_button, catch_button, change_color_button]
    input_boxes = [input_box1, input_box2, input_box3, input_box4]

    def print_figures_list(self, list_figures):
        height = 20
        for figure in list_figures:
            self.GAME_FONT.render_to(self.screen, (20, height), figure.text, (255, 250, 240))
            height += 30

    def draw(self):
        for figure in self.parsers.parsed_figures:
            figure.draw(self.cairo_surface)
            pygame_surface = pygame.image.frombytes(self.cairo_surface.get_data().tobytes(),
                                                    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT), "BGRA")
            self.screen.blit(pygame_surface, (0, 0))
            pygame.display.flip()
            sleep(3)
        sleep(5)
        self.parsers.parsed_figures.clear()
        self.cairo_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            for box in self.input_boxes:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.catch_button.rect.collidepoint(event.pos):
                        self.parsers.parsed_inputs.append(box.text)
                box.handle_event(event, self.catch_button)
                box.update()
                box.draw(self.screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.change_color_button.rect.collidepoint(event.pos):
                    self.colors.change_color(self.color_input_box.text)
                if self.draw_all_button.rect.collidepoint(event.pos):
                    self.draw()
            self.color_input_box.handle_event(event, self.change_color_button)
            self.color_input_box.update()
            self.color_input_box.draw(self.screen)

    def main(self):
        while True:
            self.screen.fill("black")
            self.input_box1.show(self.screen, self.GAME_FONT)
            self.input_box2.show(self.screen, self.GAME_FONT)
            self.input_box3.show(self.screen, self.GAME_FONT)
            self.input_box4.show(self.screen, self.GAME_FONT)
            self.color_input_box.show(self.screen, self.GAME_FONT)
            self.change_color_button.show()
            self.catch_button.show()
            self.draw_all_button.show()
            if len(self.parsers.parsed_inputs) == 4:
                self.parsers.input_parsing(self.parsers.parsed_inputs)
            if len(self.parsers.parsed_figures) > 0:
                self.print_figures_list(self.parsers.parsed_figures)

            self.input()

            self.change_color_button.button_activity()
            self.catch_button.button_activity()
            self.draw_all_button.button_activity()
            pygame.display.update()


if __name__ == '__main__':
    Engine2D().main()
