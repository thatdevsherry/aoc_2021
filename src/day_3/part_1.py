from io import TextIOWrapper
import numpy as np
from typing import Tuple


def process_input(input_array: np.ndarray) -> Tuple[int, int]:
    _, number_of_columns = input_array.shape
    highest_frequency, lowest_frequency = [], []

    for column in range(number_of_columns):
        column_values = input_array[:, column]
        result = np.bincount(column_values)
        highest_frequency.append(np.argmax(result))
        lowest_frequency.append(np.argmin(result))

    highest_freq_combind = int(''.join(map(str, highest_frequency)), 2)
    lowest_freq_combined = int(''.join(map(str, lowest_frequency)), 2)
    return (highest_freq_combind, lowest_freq_combined)


def run_part_1(input: TextIOWrapper) -> int:
    normal_list = []

    for line in input.readlines():
        if line[-1] == "\n":
            line = line[:-1]
        normal_list.append(list(line))

    input_array_cleansed = np.array(normal_list).astype(np.int8)
    (highest, lowest) = process_input(input_array_cleansed)
    return highest * lowest
