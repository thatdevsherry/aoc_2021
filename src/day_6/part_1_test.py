from .part_1 import run_part_1


def test_example_part_1_18_days():
    output: int | None = None
    with open("./inputs/day_6/example.txt") as example_file:
        output = run_part_1(example_file, 18)
    assert output == 26


def test_example_part_1_80_days():
    output: int | None = None
    with open("./inputs/day_6/example.txt") as example_file:
        output = run_part_1(example_file, 80)
    assert output == 5934


def test_part_1():
    output: int | None = None
    with open("./inputs/day_6/aoc_input.txt") as aoc_input_file:
        output = run_part_1(aoc_input_file, 80)
    print(f"Day 6, part 1: {output}")
