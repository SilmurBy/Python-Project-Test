import pygame

from map_and_path_generation import map_builder


class BoardMetrics:
    def __init__(self, area, board):
        self.area = area
        self.spacing = 1
        self.left = area[0] + self.spacing
        self.top = area[1] + self.spacing
        self.width = area[2] - area[0] * self.spacing
        self.height = area[3] - area[1] * self.spacing
        self.num_y = board.get_size()[1]
        self.num_x = board.get_size()[0]
        self.cy = self.height / self.num_y
        self.cx = self.width / self.num_x

    def cell_rect(self, pos):
        return [self.left + pos[0] * self.cx, self.top + pos[1] * self.cy, self.cx - self.spacing,
                self.cy - self.spacing]

    def cell_center(self, pos):
        rct = self.cell_rect(pos)
        return [rct[0] + rct[2] / 2, rct[1] + rct[3] / 2]


def draw_board(surface, area, board):
    pygame.draw.rect(surface, (0, 0, 0), area)
    metrics = BoardMetrics(area, board)

    colors = {
        map_builder.CellType.Sea: (0, 0, 255),
        map_builder.CellType.Land: (0, 255, 0),
    }
    marks = {
        map_builder.CellMark.Start: (255, 0, 255),
        map_builder.CellMark.End: (255, 0, 0),
    }
    for y in range(0, metrics.num_y):
        for x in range(0, metrics.num_x):
            cell = board.at([x, y])
            clr = colors.get(cell.type, cell.type)
            cell_rect = metrics.cell_rect([x, y])

            pygame.draw.rect(surface, clr, cell_rect)

            mark = marks.get(cell.mark)
            if mark != None:
                pygame.draw.rect(surface, mark, cell_rect, 10)


def draw_path(surface, area, board, path):
    metrics = BoardMetrics(area, board)
    for i in range(0, len(path) - 1):
        ctr_a = metrics.cell_center(path[i].pos)
        ctr_b = metrics.cell_center(path[i + 1].pos)
        pygame.draw.line(surface, (255, 255, 0), ctr_a, ctr_b, 5)


