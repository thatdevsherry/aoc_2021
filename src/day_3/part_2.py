from io import TextIOWrapper
import numpy as np
from typing import Literal
from enum import Enum


class LifeSupportRating(Enum):
    OXYGEN = "OXYGEN"
    CO2 = "CO2"


def process_input(input_array: np.ndarray, reading_type: Literal["OXYGEN", "CO2"]) -> int:
    _, number_of_columns = input_array.shape
    array_to_narrow = input_array

    for column in range(number_of_columns):
        column_values = input_array[:, column]
        if reading_type == LifeSupportRating.OXYGEN.value:
            frequency_digit: int = np.argmax(np.bincount(column_values))
        else:
            frequency_digit: int = np.argmin(np.bincount(column_values))

        if len(array_to_narrow) == 1:
            break

        if len(array_to_narrow) == 2:
            if reading_type == LifeSupportRating.OXYGEN.value:
                if array_to_narrow[array_to_narrow[:, column] == 1].size > 0:
                    array_to_narrow = array_to_narrow[array_to_narrow[:,
                                                                      column] == 1]
            else:
                if array_to_narrow[array_to_narrow[:, column] == 0].size > 0:
                    array_to_narrow = array_to_narrow[array_to_narrow[:,
                                                                      column] == 0]

        if len(array_to_narrow[array_to_narrow[:, column] == frequency_digit]) != 0:
            array_to_narrow = array_to_narrow[array_to_narrow[:,
                                                              column] == frequency_digit]
        else:
            continue

    return array_to_narrow[0]


def run_part_2(input: TextIOWrapper):
    normal_list = []

    for line in input.readlines():
        if line[-1] == "\n":
            line = line[:-1]
        normal_list.append(list(line))

    input_array_cleansed = np.array(normal_list).astype(np.int8)
    oxygen_generator_rating = process_input(
        input_array_cleansed, LifeSupportRating.OXYGEN.value)
    co2_scrubber_rating = process_input(
        input_array_cleansed, LifeSupportRating.CO2.value)
    oxygen_generator_rating_as_decimal = int(
        ''.join(map(str, oxygen_generator_rating)), 2)
    co2_scrubber_rating_as_decimal = int(
        ''.join(map(str, co2_scrubber_rating)), 2)
    return oxygen_generator_rating_as_decimal * co2_scrubber_rating_as_decimal
