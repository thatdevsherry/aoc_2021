from io import TextIOWrapper
from .part_1 import SubmarineSimulator, DepthDirection, SpeedDirection


class SubmarineSimulator(SubmarineSimulator):
    aim: int = 0

    def change_depth(self, value: int, direction: DepthDirection):
        if direction == DepthDirection.UP.value:
            self.aim -= int(value)
        else:
            self.aim += int(value)

    def change_horizontal_position(self, value: int, direction: SpeedDirection):
        if direction == SpeedDirection.FORWARD.value:
            self.horizontal_position += int(value)
            self.depth += self.aim * int(value)


def run_part_2(input: TextIOWrapper):
    simulator = SubmarineSimulator()

    for line in input.readlines():
        simulator.process_command(line)

    return simulator.multiply_horizontal_position_and_depth()
