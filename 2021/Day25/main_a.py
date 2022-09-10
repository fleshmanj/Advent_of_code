from enum import Enum
from data import raw_input
from copy import deepcopy


class Seafloor_placeholder(Enum):
    EMPTY = 0
    SOUTH_CUC = 1
    EAST_CUC = 2


class Inputhandler:

    def __init__(self):
        pass

    @staticmethod
    def generate_map_floor(data: str) -> list:
        rows = []
        lines = data.split("\n")
        for line in lines:
            temp = []
            for character in line:
                if character == ".":
                    temp.append(Seafloor_placeholder.EMPTY)
                elif character == "v":
                    temp.append(Seafloor_placeholder.SOUTH_CUC)
                elif character == ">":
                    temp.append(Seafloor_placeholder.EAST_CUC)
                else:
                    raise NotImplemented
            rows.append(temp)
        return rows


class Map:
    height: int
    width: int
    grid: list[list[Seafloor_placeholder]]

    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def move_east_cucs(self) -> bool:
        new_grid = deepcopy(self.grid)
        moved = False
        for row in range(len(self.grid)):
            col = self.width - 1
            rolled = False
            while col != -1:
                if col == self.width - 1:
                    if self.grid[row][col] is Seafloor_placeholder.EMPTY:
                        if self.grid[row][col - 1] == Seafloor_placeholder.EAST_CUC:
                            new_grid[row][col] = Seafloor_placeholder.EAST_CUC
                            new_grid[row][col - 1] = Seafloor_placeholder.EMPTY
                            rolled = True
                            moved = True
                if col != 0:
                    if self.grid[row][col] is Seafloor_placeholder.EMPTY:
                        if self.grid[row][col - 1] == Seafloor_placeholder.EAST_CUC:
                            new_grid[row][col] = Seafloor_placeholder.EAST_CUC
                            new_grid[row][col - 1] = Seafloor_placeholder.EMPTY
                            moved = True
                if not rolled:
                    if col == 0:
                        if self.grid[row][col] is Seafloor_placeholder.EMPTY:
                            if self.grid[row][col - 1] is Seafloor_placeholder.EAST_CUC:
                                new_grid[row][col] = Seafloor_placeholder.EAST_CUC
                                new_grid[row][col - 1] = Seafloor_placeholder.EMPTY
                                moved = True
                col -= 1
        self.grid = new_grid
        return moved

    def move_south_cucs(self) -> bool:
        new_grid = deepcopy(self.grid)
        moved = False
        for col in range(self.width):
            row = self.height - 1
            rolled = False
            while row != -1:
                if row == self.height - 1:
                    if self.grid[row][col] is Seafloor_placeholder.EMPTY:
                        if self.grid[self.height - 1][col] is Seafloor_placeholder.SOUTH_CUC:
                            new_grid[row][col] = Seafloor_placeholder.SOUTH_CUC
                            new_grid[self.height - 1][col] = Seafloor_placeholder.EMPTY
                            rolled = True
                            moved = True
                if row != 0:
                    if self.grid[row][col] is Seafloor_placeholder.EMPTY:
                        if self.grid[row - 1][col] is Seafloor_placeholder.SOUTH_CUC:
                            new_grid[row][col] = Seafloor_placeholder.SOUTH_CUC
                            new_grid[row - 1][col] = Seafloor_placeholder.EMPTY
                            moved = True
                if not rolled:
                    if row == 0:
                        if self.grid[row][col] is Seafloor_placeholder.EMPTY:
                            if self.grid[row - 1][col] is Seafloor_placeholder.SOUTH_CUC:
                                new_grid[row][col] = Seafloor_placeholder.SOUTH_CUC
                                new_grid[row - 1][col] = Seafloor_placeholder.EMPTY
                                moved = True
                row -= 1
        self.grid = new_grid
        return moved

    def print_grid(self) -> None:
        print("\n")
        for row in self.grid:
            line = ""
            for i in row:
                if i.value == 0:
                    line = line + "."
                if i.value == 1:
                    line = line + "v"
                if i.value == 2:
                    line = line + ">"
            print(line)


if __name__ == "__main__":
    ...
    i = Inputhandler
    m = Map(i.generate_map_floor(raw_input))
    moving = True
    runs = 0
    while moving:
        runs += 1
        east_cucs_moved = m.move_east_cucs()
        south_cucs_moved = m.move_south_cucs()
        if not east_cucs_moved and not south_cucs_moved:
            moving = False
    m.print_grid()
    print(runs)
