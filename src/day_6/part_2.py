"""
So yeah, Python data models were nice for part 1, but part 2 became
computationally expensive, and the time to run the test for 256 days was taking
so long I had to exit out.

Let's solve this part using numpy array.

My first iteration is super bad, the fish increase exponentially so the code
still is really, really slow. I don't think it even outputs the answer :P

Will have to figure out a better way.
"""
from io import TextIOWrapper
import numpy as np


def run_stuff(lanternfish_school):
    lanternfish_school = np.array([lanternfish_school])
    # check for 0s, and store their indices
    zeros_on_current_day = lanternfish_school == 0
    # decrement all values not currently 0
    lanternfish_school[lanternfish_school != 0] -= 1
    # replace zeros (from first step) with 6
    lanternfish_school[np.where(zeros_on_current_day)[0]] = 6
    # for each 0 from step 1, add a new value 8
    lanternfish_school = np.append(lanternfish_school, np.repeat(
        8, np.where(zeros_on_current_day)[0].size))
    return lanternfish_school


def run_part_2(input: TextIOWrapper, days: int) -> int:
    input_cleansed = list(map(int, input.read().strip("\n").split(",")))
    lanternfish_school = np.array(input_cleansed)

    for _ in range(0, days):
        lanternfish_school = np.concatenate(
            list(map(run_stuff, lanternfish_school)))
    return lanternfish_school.size
