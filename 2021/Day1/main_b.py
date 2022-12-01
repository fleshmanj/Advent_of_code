from main_a import DepthFinder, InputHandler


class UpgradedInputHandler(InputHandler):

    def make_list_of_depth_measurements(self) -> None:
        temp = self.data_in.split("\n")
        print(temp)

        for line in range(0, len(temp)):
            if line < len(temp) - 2:
                sum = int(temp[line]) + int(temp[line + 1]) + int(temp[line + 2])
                print(int(temp[line]), int(temp[line + 1]), int(temp[line + 2]))
                self.data_out.append(sum)
        print(len(self.data_out))
        # for line in temp:
        #     line = line.split(" ")
        #     self.data_out.append(int(line[0]))
