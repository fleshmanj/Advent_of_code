class File:
    name: str
    size: int
    contents: []

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.contents = []


class Directory:

    def __init__(self):
        self.directory = {"/": {}}
        self.working_directory = "/"
        self.cd = self.directory["/"]

    def cd(self, dir):
        self.working_directory = self.working_directory + "/" + dir
        self.cd = self.cd[dir]
        print(self.working_directory)

    def add_dir(self, dir):
        self.cd[dir] = {}

    def show_dir(self):
        print(self.directory)

    def cd_up(self):
        pass


class InputHandler:
    data: str
    directory: Directory

    def __init__(self, data):
        self.directory = Directory()
        self.data = data
        self.log = []
        self.parse_data()

    def parse_data(self):
        self.log = self.data.splitlines()

    def show_commands(self):
        for line in self.log:
            if line.startswith("$"):
                print(line)
            if line.startswith("dir"):
                print(line)

    def build_dir(self):
        for line in self.log:
            # if line.startswith("$ ls"):
            #     print(line)
            if line.startswith("dir"):
                self.directory.add_dir(line[4:])
            if line.startswith("$ cd "):
                if line == "$ cd ..":
                    self.directory.cd_up()
                elif line == "$ cd /":
                    pass
                else:
                    if line[4:] not in self.directory.cd.keys():
                        self.directory.add_dir(line[5:])
                    else:
                        pass


