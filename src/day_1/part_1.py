from io import TextIOWrapper


def run_part_1(input_file: TextIOWrapper) -> int:
    counter = 0
    previous_value: int | None = None
    for line in input_file.readlines():
        line_data = int(line)

        if previous_value is not None and line_data > previous_value:
            counter += 1

        # whatever happens, we update previous value before next loop
        previous_value = line_data
    return counter
