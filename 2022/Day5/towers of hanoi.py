class Towers:

    def __init__(self, n):
        self.discs = n
        self.towers = [[]]*3
        self.towers[0] = [i for i in range(n, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []

    def move(self, source, dest):
        dest.append(source.pop())


def solve_towers(n, towers, start_tower, dest_tower, aux_tower):
    if n == 0:
        return

    solve_towers(n - 1, towers, start_tower, aux_tower, dest_tower)

    towers.move(start_tower, dest_tower)

    solve_towers(n - 1, towers, aux_tower, dest_tower, start_tower)


towers = Towers(3)

solve_towers(towers.discs, towers, towers.towers[0], towers.towers[2], towers.towers[1])
print(towers.towers)
