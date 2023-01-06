from .part_1 import run_part_1


def test_example_part_1():
    output: int | None = None
    with open("./inputs/day_7/example.txt") as example_file:
        output = run_part_1(example_file)
    assert output == 37


def test_part_1():
    output: int | None = None
    with open("./inputs/day_7/aoc_input.txt") as aoc_input_file:
        output = run_part_1(aoc_input_file)
    print(f"Day 7, part 1: {output}")
