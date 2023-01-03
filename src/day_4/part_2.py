from .part_1 import Bingo
from io import TextIOWrapper


class Bingo(Bingo):
    def _mark_number(self, move: int) -> int | None:
        sum_of_final_board: int | None = None
        completed_boards = []
        for idx, board in enumerate(self.boards):
            board.mark_number(move)
            potential_winner = board.has_won()
            if potential_winner is not None:
                if len(self.boards) == 1:
                    sum_of_final_board = potential_winner
                    break
                completed_boards.append(idx)

        # learned something, pop off multiple indices in reverse order
        # because in asc order, it would remove one index, and the new array
        # would have smaller length, so the next index to pop would be wrong.
        #
        # In reverse order, we pop off from the end and will not throw off
        # the index numbers :D
        for i in sorted(completed_boards, reverse=True):
            self.boards.pop(i)
        return sum_of_final_board

    def calculate_last_board_winner_score(self):
        winner_score: int | None = None
        for i in self.moves:
            mark_number_result = self._mark_number(i)
            if mark_number_result is not None:
                winner_score = mark_number_result * i
                break
        return winner_score


def run_part_2(input: TextIOWrapper):
    file_contents = input.read().split("\n")
    bingo_moves = list(map(int, file_contents[0].split(",")))

    board_entries = list(filter(lambda k: k != "", file_contents[2:]))
    board_entries_cleaned = [
        list(map(int, filter(lambda k: k != "", entry.split(" ")))) for entry in board_entries]

    play_instance = Bingo(bingo_moves, board_entries_cleaned)
    return play_instance.calculate_last_board_winner_score()
