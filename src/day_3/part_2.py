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
    value_to_find_in_array = []

    for col in range(number_of_columns):
        if len(array_to_narrow) == 1:
            value_to_find_in_array = array_to_narrow[0]
            break

        column_values = array_to_narrow[:, col]
        result = np.bincount(column_values)
        if reading_type == LifeSupportRating.OXYGEN.value:
            highest_frequency_number = np.argmax(
                result) if result[0] != result[1] else 1
            array_to_narrow = array_to_narrow[np.where(
                array_to_narrow[:, col] == highest_frequency_number)]
            value_to_find_in_array.append(highest_frequency_number)
        else:
            lowest_frequency_number = np.argmin(
                result) if result[0] != result[1] else 0
            array_to_narrow = array_to_narrow[np.where(
                array_to_narrow[:, col] == lowest_frequency_number)]
            value_to_find_in_array.append(lowest_frequency_number)

    return int(''.join(map(str, value_to_find_in_array)), 2)


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
    return oxygen_generator_rating * co2_scrubber_rating
