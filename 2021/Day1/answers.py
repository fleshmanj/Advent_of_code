from main_a import DepthFinder, InputHandler, OutputHandler
from data import raw_input

d = DepthFinder()
i = InputHandler(raw_input, d)
o = OutputHandler(d, i.data_out)
o.read_measurements()
o.show_results(d)
