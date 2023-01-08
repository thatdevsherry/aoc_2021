from io import TextIOWrapper
from typing import List, Union


class SyntaxChecker:
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    scores = [3, 57, 1197, 25137]
    pairs_by_closing = dict(zip(closing, opening))
    scoring = dict(zip(closing, scores))

    inputs_raw: List[str]
    score: int

    def __init__(self, inputs: List[str]):
        self.score = 0
        self.inputs_raw = inputs

    def run(self) -> int:
        """
        Runs syntax checker and returns score of corruptions.
        """
        detection_results = [self.detect_corruption(
            i) for i in self.inputs_raw]
        corruptions = [i for i in detection_results if i is not None]
        corruptions_score = [self.scoring.get(i) for i in corruptions]
        self.score = sum(corruptions_score)
        return sum(corruptions_score)

    def detect_corruption(self, chunk: str) -> Union[str, None]:
        stack = [chunk[0]]

        for c in chunk[1:]:
            if len(stack) == 0 and c in self.closing:
                # somehow the stack is empty and we're still in loop,
                # CORRUPTION
                return c
            if c in self.opening:
                stack.append(c)
                continue
            # if the char being read is the closing pair of the char on top
            # of stack
            if self.pairs_by_closing.get(c) == stack[-1]:
                stack.pop()
                continue

            # if char being read is a closing one but isn't matching the one
            # on top of stack, it is incorrect and we are to yeet.
            if c in self.closing and self.pairs_by_closing.get(c) != stack[-1]:
                # YEET
                return c


def run_part_1(input: TextIOWrapper) -> int:
    input = [i.strip("\n").split("\n")[0] for i in input.readlines()]
    checker = SyntaxChecker(input)
    checker.run()
    return checker.score
