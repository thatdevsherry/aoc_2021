from io import TextIOWrapper
import numpy as np


def gauss_distance(num):
    return num * (num + 1)/2


def run_part_2(input: TextIOWrapper) -> int:
    input_cleansed = np.array(
        list(map(int, input.read().strip("\n").split(","))))
    print(input_cleansed)
