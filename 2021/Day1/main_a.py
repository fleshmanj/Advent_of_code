class DepthFinder:
    current_depth: int
    previous_depth: int | None
    recorded_increase: int
    recorded_decrease: int

    def __init__(self):
        self.current_depth = 0
        self.previous_depth = None
        self.recorded_increase = 0
        self.recorded_decrease = 0

    def read_depth(self, measurement: int) -> None:
        if self.previous_depth is None:
            self.calibrate(measurement)
        self.current_depth = measurement
        if self.current_depth > self.previous_depth:
            self.ping_increase()
        if self.current_depth < self.previous_depth:
            self.ping_decrease()
        self.previous_depth = self.current_depth

    def ping_increase(self) -> None:
        self.recorded_increase += 1

    def ping_decrease(self) -> None:
        self.recorded_decrease += 1

    def calibrate(self, measurement: int) -> None:
        self.previous_depth = measurement


class InputHandler:
    data_in: str
    data_out: list[int]
    depth_finder: DepthFinder

    def __init__(self, data_in: str, depth_finder: DepthFinder) -> None:
        self.depth_finder = depth_finder
        self.data_in = data_in
        self.data_out = []
        self.make_list_of_depth_measurements()

    def make_list_of_depth_measurements(self) -> None:
        temp = self.data_in.split("\n")
        for line in temp:
            line = line.split(" ")
            self.data_out.append(int(line[0]))


class OutputHandler:
    depth_finder: DepthFinder
    data_in: list[int]

    def __init__(self, depth_finder: DepthFinder, data_in: list):
        self.depth_finder = depth_finder
        self.data_in = data_in

    def read_measurements(self) -> None:
        for measurement in self.data_in:
            self.depth_finder.read_depth(measurement)

    def show_results(self) -> None:
        print(f"\nThe total recorded increases in depth is {self.depth_finder.recorded_increase} times.")
        print(f"\nThe total recorded decreases in depth is {self.depth_finder.recorded_decrease} times.")
