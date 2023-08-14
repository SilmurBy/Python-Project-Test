import re

import pygame

from map_and_path_generation import map_builder, path_builder
from map_and_path_generation.draw import draw_board, draw_path


class Engine2D:
    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("Engine2D for path finding")
    clock = pygame.time.Clock()

    def __init__(self):
        self.path = None
        self.board = None

    def set_board(self, board):
        self.board = board

    def set_path(self, path):
        self.path = path

    def draw_main_board(self, surface):
        if self.board is None:
            return
        draw_board(surface, surface.get_rect(), self.board)
        pygame.display.flip()

    def draw_main_path(self, surface):
        if self.path is not None:
            draw_path(surface, surface.get_rect(), self.board, self.path)
        pygame.display.flip()

    def step(self, steps):
        pass

    def reset(self):
        pass

    def coordinate_parsing(self, message):
        input_cached = input(message)
        coordinate = re.findall('[0-9]+', input_cached)
        if type(coordinate) == list and len(coordinate) == 2:
            if coordinate[0].isdigit() and coordinate[1].isdigit():
                x = int(coordinate[0])
                y = int(coordinate[1])
                if x >= 0 and y >= 0:
                    return [x, y]

    def main(self):
        x = input("Enter column count: ")
        y = input("Enter row count: ")
        field = map_builder.create_field(int(x), int(y))
        self.set_board(field.board)
        self.draw_main_board(self.screen)
        while True:
            self.clock.tick()

            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
                if event.key == pygame.K_RETURN:
                    start = self.coordinate_parsing("Enter coordinates of start: ")
                    finish = self.coordinate_parsing("Enter coordinates of finish: ")
                    filled = path_builder.fill_shortest_path(self.board, start, finish)
                    path = path_builder.backtrack_to_start(filled, finish)
                    self.set_board(filled)
                    self.set_path(path)
                    self.draw_main_board(self.screen)
                    self.draw_main_path(self.screen)
                if event.key == pygame.K_r:
                    self.reset()



            self.clock.tick(60)
            pygame.display.update()


if __name__ == '__main__':
    Engine2D().main()
