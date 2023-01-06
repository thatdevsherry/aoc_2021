from .part_2 import run_part_2
import pytest


def test_example_part_2_after_256_days():
    output: int | None = None
    with open("./inputs/day_6/example.txt") as example_file:
        output = run_part_2(example_file, 256)
    assert output == 26984457539


@pytest.mark.skip
def test_part_2():
    output: int | None = None
    with open("./inputs/day_6/aoc_input.txt") as aoc_input_file:
        output = run_part_2(aoc_input_file, 256)
    print(f"Day 6, part 2: {output}")
