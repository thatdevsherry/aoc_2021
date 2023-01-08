from io import TextIOWrapper
from .part_1 import SyntaxChecker
from typing import Union, List
import numpy as np


class SyntaxCheckerImproved(SyntaxChecker):
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    scores = [1, 2, 3, 4]
    pairs_by_opening = dict(zip(opening, closing))
    scoring = dict(zip(closing, scores))

    def calculate_score_of_incomplete_strings(
            self,
            incomplete_pair: str
    ) -> np.ndarray:
        total_score = 0
        for i in incomplete_pair:
            closing_pair = self.pairs_by_opening.get(i)
            closing_pair_score = self.scoring.get(closing_pair)
            total_score = (total_score * 5) + closing_pair_score
        return total_score

    def run(self) -> int:
        """
        Runs syntax checker and returns score of corruptions.
        """
        detection_results = [self.detect_incomplete(
            i) for i in self.inputs_raw]
        incomplete_results = [i for i in detection_results if i is not None]
        all_scores = np.array([self.calculate_score_of_incomplete_strings(
            i) for i in incomplete_results])
        self.score = int(np.median(np.sort(all_scores)))
        return np.median(np.sort(all_scores))

    def detect_incomplete(self, chunk: str) -> Union[str, None]:
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
                return None

        x = ''.join(stack)
        return x[::-1]


def run_part_2(input: TextIOWrapper) -> int:
    input = [i.strip("\n").split("\n")[0] for i in input.readlines()]
    checker = SyntaxCheckerImproved(input)
    checker.run()
    return checker.score
