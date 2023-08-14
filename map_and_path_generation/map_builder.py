import random, types, copy
from enum import Enum


class CellType(Enum):
    Sea = 1
    Land = 2


class CellMark(Enum):
    No = 0
    Start = 1
    End = 2


class Cell:
    def __init__(self, type=CellType.Sea, pos=None):
        self.type = type
        self.count = 0
        self.mark = CellMark.No
        self.path_from = None
        self.pos = pos


class CellGrid:
    def __init__(self, board):
        self.board = board

    def get_size(self):
        return [len(self.board), len(self.board[0])]

    def at(self, pos):
        return self.board[pos[0]][pos[1]]

    def clone(self):
        return CellGrid(copy.deepcopy(self.board))

    def clear_count(self, count):
        for o in self.board:
            for i in o:
                i.count = count
                i.path_from = None

    def is_valid_point(self, pos):
        sz = self.get_size()
        return 0 <= pos[0] < sz[0] and 0 <= pos[1] < sz[1]


def create_empty_maze(x, y):
    return types.SimpleNamespace(
        board=CellGrid([[Cell(type=CellType.Sea, pos=[ix, iy]) for iy in range(y)] for ix in range(x)]),
        start=[random.randrange(0, x), random.randrange(0, y)],
        end=[random.randrange(0, x), random.randrange(0, y)])


def count_alive_neighbours(board, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbour_x = x + i
            neighbour_y = y + j
            if i == 0 and j == 0:
                pass
            elif neighbour_x < 0 or neighbour_y < 0 or neighbour_x >= len(board) or neighbour_y >= len(board[0]):
                pass
            elif board[neighbour_x][neighbour_y].type == CellType.Land:
                count = count + 1
    return count


def next_generation_lands(board, count_cell):
    new_board = copy.deepcopy(board)
    count_land = 0
    target_land = count_cell / 100 * 30
    target_range = count_cell / 100 * 0.1
    for x in range(len(board)):
        for y in range(len(board[x])):
            count_land_neighbours = count_alive_neighbours(board, x, y)
            if board[x][y].type == CellType.Land:
                if count_land_neighbours < 3:
                    new_board[x][y] = Cell(type=CellType.Sea, pos=[x, y])
                else:
                    new_board[x][y] = Cell(type=CellType.Land, pos=[x, y])
            else:
                if count_land_neighbours > 3:
                    new_board[x][y] = Cell(type=CellType.Land, pos=[x, y])
                else:
                    new_board[x][y] = Cell(type=CellType.Sea, pos=[x, y])
            if new_board[x][y].type == CellType.Land:
                count_land += 1
            if count_land >= target_land and abs(count_land - target_land) < target_range:
                break
    land_percent = (count_land / count_cell) * 100
    return new_board, land_percent


def generation_runner(board, x, y):
    count_cell = x * y
    land_percent = 0
    while land_percent < 30 or land_percent == 0:
        board, land_percent_new = next_generation_lands(board, count_cell)
        if land_percent_new == land_percent or (land_percent_new < 10 and land_percent != 0):
            break
        land_percent = land_percent_new
    return board, land_percent


def create_field(x, y):
    fill_variant = 0.28
    if x < 20 or y < 20:
        fill_variant = 0.35
    if x > 250 or y > 250:
        fill_variant = 0.29
    board = [[0] * y for _ in range(x)]
    result_percent = 100
    while abs(result_percent - 30) > 1:
        for i in range(x):
            for j in range(y):
                r = random.random()
                board[i][j] = Cell(type=CellType.Land, pos=[i, j]) if (r < fill_variant) else Cell(type=CellType.Sea,
                                                                                                   pos=[i, j])
        board, result_percent = generation_runner(board, x, y)
    return types.SimpleNamespace(board=CellGrid(board))


def add_point(a, b):
    return [a[0] + b[0], a[1] + b[1]]
