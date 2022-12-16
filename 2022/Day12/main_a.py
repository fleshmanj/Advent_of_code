import random


class Cell:

    def __init__(self, coords, height):
        self.coords = coords
        self.height = height


class Player:

    def __init__(self, x, y):
        self.current_x = x
        self.current_y = y
        self.current_pos = (x, y)
        self.height = 0
        self.visited = []
        self.blacklist = []


class InputHandler:
    player: Player

    def __init__(self, data: str):
        self.data = data
        self.start = None
        self.target = None
        self.map_cells = {}
        self.maze = []
        self.parse_data()
        self.round = 0
        self.finished = False

    def parse_data(self):
        letters = [chr(i) for i in range(97, 97 + 26)]

        for y, line in enumerate(self.data.splitlines()):
            for x, letter in enumerate(line):
                if letter == "E":
                    self.target = Cell((x, y), 26)
                    self.map_cells[(x, y)] = Cell((x, y), 25)
                elif letter == "S":
                    self.start = Cell((x, y), -1)
                    self.player = Player(x, y)
                    self.map_cells[(x, y)] = Cell((x, y), 0)
                else:
                    self.map_cells[(x, y)] = Cell((x, y), letters.index(letter))

        for line in self.data.splitlines():
            self.maze.append([letters.index(letter) if letter.islower() else ord(letter) for letter in line])

    @staticmethod
    def adjacent_cells(cell):
        possible_moves = [(cell[0] + 1, cell[1]), (cell[0] - 1, cell[1]),
                          (cell[0], cell[1] - 1), (cell[0], cell[1] + 1)]
        return possible_moves

    def move_to_higher_cell(self, map_cells: dict, currentNode, rootNode, visited):
        visited = visited
        visited.append(currentNode)
        self.round += 1
        if map_cells[currentNode] == self.start.coords:
            result = self.round
            self.finished = True
            return result
        else:
            cells = self.adjacent_cells(currentNode)
            random.shuffle(cells)
            for cell in cells:
                if cell in map_cells.keys():
                    if cell not in visited:
                        if map_cells[cell].height == map_cells[currentNode].height - 1 or map_cells[cell].height == \
                                map_cells[currentNode].height:
                            print(f"moved from {currentNode} to {map_cells[cell].coords}")
                            currentNode = map_cells[cell].coords
                            self.finished = False

                            return self.move_to_higher_cell(map_cells, currentNode, rootNode, visited)
                if cell == cells[-1]:
                    self.finished = False
                    return self.move_to_higher_cell(map_cells, (158, 20), (0, 20), visited)
