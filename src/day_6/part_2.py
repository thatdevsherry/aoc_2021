"""
I couldn't figure this out, started engineering it wayyy too much.

Turns out it was supposed to be super simple by using the right data structure
and flow.

Copied over code from theprimagen's video. Well I couldn't solve this on my
own... but at least I learned to try thinking differently :)

Vid ref: https://youtu.be/__gDZny1uwY
"""
from io import TextIOWrapper
import numpy as np
from collections import defaultdict


def run_part_2(input: TextIOWrapper, days: int) -> int:
    input_cleansed = list(map(int, input.read().strip("\n").split(",")))

    # initial setup
    lanternfish_school = np.array(input_cleansed)
    print(lanternfish_school)
    dd = defaultdict(int)
    for i in range(9):
        dd[i] = 0
    print(dd)
    for i in lanternfish_school:
        dd[i] += 1
    print(dd)

    # start work
    for _ in range(days):
        fish_at_zero = dd[0]
        dd[0] = 0
        for i in range(1, 10):
            dd[i - 1] += dd[i]
            dd[i] = 0
        dd[8] = fish_at_zero
        dd[6] += fish_at_zero

    return np.sum(np.array(list(dd.values())))
