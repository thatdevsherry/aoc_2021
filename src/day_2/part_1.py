from io import TextIOWrapper
from typing import Literal
from enum import Enum


class DepthDirection(Enum):
    UP = "up"
    DOWN = "down"


class SpeedDirection(Enum):
    FORWARD = "forward"


class SubmarineSimulator:
    horizontal_position: int = 0
    depth: int = 0

    depth_direction = [member.value for member in DepthDirection]
    horizontal_direction = [member.value for member in SpeedDirection]

    def __init__(self, horizontal_position=None, depth=None):
        pass

    def change_depth(self, value: int, direction: DepthDirection):
        if direction == DepthDirection.UP.value:
            self.depth -= int(value)
        else:
            self.depth += int(value)

    def change_horizontal_position(self, value: int, direction: SpeedDirection):
        if direction == SpeedDirection.FORWARD.value:
            self.horizontal_position += int(value)

    def process_command(self, command: str):
        if command[-1] == "\n":
            command = command[:-1]

        command = command.split(" ")
        assert len(command) == 2
        direction, direction_value = command[0], command[1]
        if direction in self.depth_direction:
            self.change_depth(direction_value, direction)
        elif direction in self.horizontal_direction:
            self.change_horizontal_position(direction_value, direction)
        else:
            pass

    def __repr__(self):
        return f"SubmarineSimulator({self.horizontal_position}, {self.depth})"

    def multiply_horizontal_position_and_depth(self):
        return self.horizontal_position * self.depth


def run_part_1(input: TextIOWrapper):
    simulator = SubmarineSimulator()

    for line in input.readlines():
        simulator.process_command(line)

    return simulator.multiply_horizontal_position_and_depth()
