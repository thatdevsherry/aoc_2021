from io import TextIOWrapper
import numpy as np


def run_part_2(input: TextIOWrapper) -> int:
    counter = 0
    previous_window: int | None = None
    input_array: np.ndarray = np.array(input.read().splitlines())
    slide_window_view = np.lib.stride_tricks.sliding_window_view(
        input_array, 3)
    for window in slide_window_view:
        window_int: np.ndarray = window.astype(np.int32)
        if previous_window is not None:
            current_window_sum: int = np.sum(window_int)
            previous_window_sum: int = np.sum(previous_window)
            if current_window_sum > previous_window_sum:
                counter += 1

        previous_window = window_int
    return counter
