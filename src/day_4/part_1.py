from io import TextIOWrapper
from typing import List
import numpy as np


class Board:
    numbers: np.ndarray
    marked: np.ndarray

    def __init__(self, numbers: List[int]):
        self.numbers = np.array(numbers)
        self.marked = np.full(self.numbers.shape, False)

    def __repr__(self):
        return f"Board({self.numbers!r})"

    def mark_number(self, move: int) -> bool:
        """
        If provided move number is present on board, it'll mark it as True.

        **Note**: that it does not automatically inform if any row or column
        gets fully marked.
        """
        # find the number on the board
        index_of_number_on_board = np.where(self.numbers == move)

        # if not found, return
        if len(index_of_number_on_board[0]) == 0:
            return False

        # update the same index in self.marked and set the value to True
        self.marked[index_of_number_on_board[0],
                    index_of_number_on_board[1]] = True
        return True

    def has_won(self) -> int | None:
        """
        Checks if board has any row or column fully marked.

        Returns sum of marked numbers if board has won, otherwise returns None.
        """
        # Check rows first
        for idx, row in enumerate(self.marked):
            if np.all(row):
                # remove all numbers that were previously marked,
                # including ones that are not in the winning row/col
                unmarked_numbers = self.numbers[np.invert(self.marked)]
                return np.sum(unmarked_numbers)

        # Check columns second
        for row in np.transpose(self.marked):
            if np.all(row):
                # remove all numbers that were previously marked,
                # including ones that are not in the winning row/col
                unmarked_numbers = self.numbers[np.invert(self.marked)]
                return np.sum(unmarked_numbers)
        return None


class Bingo:
    moves: List[int]
    boards: List[Board]

    def _setup_boards(self, board_entries: List[List[int]]) -> List[Board]:
        number_of_boards = len(board_entries) // 5
        idx = 0
        boards = []
        for i in range(number_of_boards):
            boards.append(Board(board_entries[idx:idx + 5]))
            idx += 5
        return boards

    def __init__(self, moves: List[int], board_entries: List[List[int]]):
        self.moves = moves
        self.boards = self._setup_boards(board_entries)

    def _mark_number(self, move: int) -> int | None:
        sum_of_marked_numbers: int | None = None
        for board in self.boards:
            board.mark_number(move)
            potential_winner = board.has_won()
            if potential_winner is not None:
                sum_of_marked_numbers = potential_winner
                break
        return sum_of_marked_numbers

    def calculate_winner_score(self) -> int:
        winner_score: int | None = None
        for i in self.moves:
            mark_number_result = self._mark_number(i)
            if mark_number_result is not None:
                winner_score = mark_number_result * i
                break
        return winner_score


def run_part_1(input: TextIOWrapper):
    file_contents = input.read().split("\n")
    bingo_moves = list(map(int, file_contents[0].split(",")))

    board_entries = list(filter(lambda k: k != "", file_contents[2:]))
    board_entries_cleaned = [
        list(map(int, filter(lambda k: k != "", entry.split(" ")))) for entry in board_entries]

    play_instance = Bingo(bingo_moves, board_entries_cleaned)
    return play_instance.calculate_winner_score()
