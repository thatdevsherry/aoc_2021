from .part_2 import run_part_2


def test_example_part_2():
    output: int | None = None
    with open("./inputs/day_4/example.txt") as example_file:
        output = run_part_2(example_file)
    assert output == 1924


def test_part_2():
    output: int | None = None
    with open("./inputs/day_4/aoc_input.txt") as aoc_input_file:
        output = run_part_2(aoc_input_file)
    print(f"Day 4, part 2: {output}")
