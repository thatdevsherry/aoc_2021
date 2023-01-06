from io import TextIOWrapper
from typing import List, Self


class Lanternfish:
    timer: int
    default_timer: int

    def __init__(self, timer: int = 6):
        self.default_timer = 6  # value after reset

        self.timer = timer

    def __repr__(self):
        return f"{self.__class__.__name__}({self.timer!r})"

    def _reset_timer(self):
        self.timer = self.default_timer

    def process_day_passed(self) -> bool:
        """
        Does stuff that is supposed to be done after a day passes.

        Returns True if new fish needs to be created, False otherwise.
        """
        if self.timer == 0:
            self._reset_timer()
            return True
        else:
            self.timer -= 1
            return False


class LanternfishSimulator:
    all_fish: List[Lanternfish]

    def __init__(self, input: List[int]):
        self.all_fish = [Lanternfish(fish_timer) for fish_timer in input]

    def run_simulation_for_days(self, days: int):
        """
        Runs simulation for the number of days provided.
        """
        for _ in range(1, days + 1):
            fish_scheduled_for_creation: int = 0

            for fish in self.all_fish:
                should_create_new_fish = fish.process_day_passed()
                if should_create_new_fish:
                    fish_scheduled_for_creation += 1

            for _ in range(fish_scheduled_for_creation):
                self.all_fish.append(Lanternfish(8))


def run_part_1(input: TextIOWrapper, days: int) -> None:
    input_cleansed = list(map(int, input.read().strip("\n").split(",")))
    lanternfish_simulator = LanternfishSimulator(input_cleansed)
    lanternfish_simulator.run_simulation_for_days(days)
    return len(lanternfish_simulator.all_fish)
