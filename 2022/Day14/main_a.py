class SandBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self) -> tuple:
        return (self.x, self.y)


class WallBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)


class InputHandler:

    def __init__(self, data: str):
        self.y_max = None
        self.y_min = None
        self.x_max = None
        self.x_min = None
        self.data = data
        self.walls = []
        self.find_walls()
        self.find_view_dimensions()
        self.source = (0, 500)

    def find_walls(self):
        for line in self.data.splitlines():
            current_vertex = None
            lines = line.split(" -> ")
            # print(lines)
            vertices = []
            for index, vert in enumerate(lines):
                x, y = vert.split(",")
                vertices.append((int(x), int(y)))

            for index, vertex in enumerate(vertices):
                if index < len(vertices) - 1:
                    if current_vertex == None:
                        current_vertex = vertex
                    next_vertex = vertices[index + 1]
                    # print(current_vertex, next_vertex)
                    # print(next_vertex[0]-current_vertex[0],next_vertex[1]-current_vertex[1])
                    x_difference = next_vertex[0] - current_vertex[0]
                    y_difference = next_vertex[1] - current_vertex[1]
                    if next_vertex[0] == current_vertex[0]:
                        for i in range(current_vertex[1], next_vertex[1] + 1):
                            self.walls.append((current_vertex[0], i))
                    if next_vertex[1] == current_vertex[1]:
                        for i in range(next_vertex[0], current_vertex[0] + 1):
                            self.walls.append((i, current_vertex[1]))
                    current_vertex = next_vertex

    def find_view_dimensions(self):
        x_nums = [coords[0] for coords in self.walls]
        y_nums = [coords[1] for coords in self.walls]
        self.x_min = min(x_nums)
        self.x_max = max(x_nums)
        self.y_min = min(y_nums)
        self.y_max = max(y_nums)

    def build_map(self):
        map = ""
        for y in range(0, self.y_max + 1):
            for x in range(self.x_min, self.x_max + 1):
                if (x, y) not in self.walls:
                    map = map + "."
                else:
                    map = map + "#"
            map = map
            map = map + str(y) + "\n"
        print(map)

    def spawn_sand_and_fall(self):
        sand = SandBlock(self.source[0], self.source[1])
        while True:
            coord = sand.get_coords()
            if (coord[0], coord[1]+1) in self.walls:
                break
            else:
                sand.y = sand.y + 1
