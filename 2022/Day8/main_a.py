class Tree:
    coords: tuple
    height: int

    def __init__(self, coords: tuple, height):
        self.coords = coords
        self.height = height
        self.visible = None
        self.edge = False
        self.viewing_distance = ()
        self.scenic_score = 0


class InputHandler:
    data: str
    trees: list
    width: int
    height: int
    vertical_edges: tuple
    horizontal_edges: tuple

    def __init__(self, data: str):
        self.data = data
        self.trees = []
        self.vertical_edges = ()
        self.parse_data()
        self.find_forest_edges()
        self.find_hidden_trees()

    def parse_data(self):
        data = self.data.splitlines()
        self.width = len(data[0])
        self.height = len(data)
        for y in range(0, len(data)):
            for x, num in enumerate(data[y]):
                self.trees.append(Tree((x, y), num))

    def find_forest_edges(self):
        self.vertical_edges = (0, self.height)
        self.horizontal_edges = (0, self.width)
        for tree in self.trees:
            if tree.coords[0] in self.horizontal_edges or tree.coords[1] in self.vertical_edges:
                tree.edge = True

    def find_hidden_trees(self):
        for tree in self.trees:
            sface_visible = True
            nface_visible = True
            wface_visible = True
            eface_visible = True

            ntree_count = 0
            stree_count = 0
            etree_count = 0
            wtree_count = 0

            # print("new tree\nNorth")

            column = self.build_column(tree.coords[0])
            row = self.build_row(tree.coords[1])

            for i in range(tree.coords[1], 0, -1):
                ntree_count += 1
                comparison_tree = column[i - 1]
                # print(f"Tree in question is at {tree.coords} with height of {tree.height} and comparison tree is at {comparison_tree.coords} with height of {comparison_tree.height}")
                if tree.height <= comparison_tree.height:
                    # print(f"Shorter than edge and tree at {column[i].coords} with height of {column[i].height}")
                    nface_visible = False
                    break

            # print("-"*40+"\nSouth")

            for i in range(tree.coords[1] + 1, self.height):
                stree_count += 1
                comparison_tree = column[i]
                # print(i)
                # print(f"Tree in question is at {tree.coords} with height of {tree.height} and comparison tree is at {comparison_tree.coords} with height of {comparison_tree.height}")
                if tree.height <= comparison_tree.height:
                    # print(f"Shorter than edge and tree at {comparison_tree.coords} with height of {comparison_tree.height}")
                    sface_visible = False
                    break

            # print("-" * 40+"\nEast")

            for i in range(tree.coords[0] + 1, self.width):
                etree_count += 1
                comparison_tree = row[i]
                # print(i)
                # print(
                #     f"Tree in question is at {tree.coords} with height of {tree.height} and comparison tree is at {comparison_tree.coords} with height of {comparison_tree.height}")
                if tree.height <= comparison_tree.height:
                    # print(
                    #     f"Shorter than edge and tree at {comparison_tree.coords} with height of {comparison_tree.height}")
                    eface_visible = False
                    break

            # print("-" * 40+"\nWest")

            for i in range(tree.coords[0], 0, -1):
                wtree_count += 1
                comparison_tree = row[i - 1]
                # print(i)
                # print(
                #     f"Tree in question is at {tree.coords} with height of {tree.height} and comparison tree is at {comparison_tree.coords} with height of {comparison_tree.height}")
                if tree.height <= comparison_tree.height:
                    # print(
                    #     f"Shorter than edge and tree at {comparison_tree.coords} with height of {comparison_tree.height}")
                    wface_visible = False
                    break

            # print(f"\nnface_visible is {nface_visible}\n"
            #       f"sface_visible is {sface_visible}\n"
            #       f"eface_visible is {eface_visible}\n"
            #       f"wface_visible is {wface_visible}\n"
            #       f"tree is at forest edge is {tree.edge}\n")

            if nface_visible or sface_visible or eface_visible or wface_visible or tree.edge:
                tree.visible = True
                tree.viewing_distance = (ntree_count,stree_count,etree_count,wtree_count)
            else:
                tree.visible = False
                tree.viewing_distance = (ntree_count, stree_count, etree_count, wtree_count)

            # print(f"tree visible is {tree.visible}")

            # print("=" * 40)

    def find_best_scenic_score(self):
        best_score = 0
        for tree in self.trees:
            tree.scenic_score = tree.viewing_distance[0]*tree.viewing_distance[1]*tree.viewing_distance[2]*tree.viewing_distance[3]
            if tree.scenic_score > best_score:
                best_score = tree.scenic_score
        print(best_score)


    def build_column(self, x_axis):
        column = []
        for tree in self.trees:
            if tree.coords[0] == x_axis:
                column.append(tree)
        return column

    def build_row(self, y_axis):
        row = []
        for tree in self.trees:
            if tree.coords[1] == y_axis:
                row.append(tree)
        return row
