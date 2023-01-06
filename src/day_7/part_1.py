from io import TextIOWrapper
import numpy as np


def run_part_1(input: TextIOWrapper) -> int:
    input_cleansed = np.array(
        list(map(int, input.read().strip("\n").split(","))))
    median = np.median(input_cleansed)
    return int(np.sum(abs(input_cleansed - median)))
