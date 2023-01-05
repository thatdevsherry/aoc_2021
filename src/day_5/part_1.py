from io import TextIOWrapper
from typing import List, Self, Literal
from itertools import chain
from collections import defaultdict


class Point:
    """
    Represents a point in our HVAS.
    """
    x: int
    y: int

    def __init__(self, x: int, y: int) -> Self:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    @staticmethod
    def from_str(s: str) -> Self:
        coordinates = list(map(int, s.split(",")))
        assert len(
            coordinates) == 2, f"expected str in form \"x,y\", received {s}"
        point = Point(coordinates[0], coordinates[1])
        return point

    def get_scalars(self):
        """
        Returns x and y values.
        """
        return [self.x, self.y]


class LineSegment:
    """
    Represents a line segment that is our main part of this problem.

    Note that it has the fields `start` and `end`, but the line segment itself
    is not a vector, so it has no sense of direction.
    """
    start: Point
    end: Point
    direction: Literal["VERTICAL", "HORIZONTAL"]

    def __init__(self, start: Point, end: Point) -> Self:
        self.start = start
        self.end = end
        self.direction = self.get_direction()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.start!r}, {self.end!r})"

    def get_direction(self):
        return "VERTICAL" if self.start.x == self.end.x else "HORIZONTAL"

    @staticmethod
    def from_str(s: str) -> Self:
        """
        Create a LineSegment instance from a text like "x1,y1 -> x2,y2"
        """
        points = s.split(" -> ")
        assert len(points) == 2
        start = Point.from_str(points[0])
        end = Point.from_str(points[1])
        line_segment = LineSegment(start, end)
        return line_segment

    def is_diagonal_line(self) -> bool:
        """
        Returns true if the line segment creates a diagonal line
        """
        return self.start.x != self.end.x and self.start.y != self.end.y

    def basis_points(self):
        """
        Returns all basis points that form the line segment.

        e.g. "1,1 -> 1,3" has three points, "(1,1), (1,2) and (1,3)"
        """
        points = []
        if self.direction == "VERTICAL":
            # vertical line
            sorted_axis = sorted([self.start.y, self.end.y])
            for i in range(sorted_axis[0], sorted_axis[1] + 1):
                basis_point = Point(self.start.x, i)
                points.append(basis_point)
        else:
            # horizontal line
            sorted_axis = sorted([self.start.x, self.end.x])
            for i in range(sorted_axis[0], sorted_axis[1] + 1):
                basis_point = Point(i, self.start.y)
                points.append(basis_point)
        return points


class HydrothermalVentsAvoidanceSystem:
    # all line segments from input
    line_segments: List[LineSegment]

    # only horizontal or vertical lines
    line_segments_filtered: List[LineSegment]

    def __init__(self, input: TextIOWrapper):
        line_segments_raw = list(
            filter(lambda k: k != "", input.read().split("\n")))
        self.line_segments = [LineSegment.from_str(
            i) for i in line_segments_raw]
        self.line_segments_filtered = [
            i for i in self.line_segments if i.is_diagonal_line() is False]

    def calculate_dangerous_points(self, overlap_threshold: int = 2) -> int:
        """
        Calculates number of overlapping points based on given threshold.

        Note that this is lazy and needs to be explicitly called.
        """
        number_of_dangerous_points = self.get_frequency_of_points()
        return number_of_dangerous_points

    def get_frequency_of_points(self, overlap_threshold: int = 2):
        all_points = self.get_basis_points_for_all_line_segments()
        point_frequencies = defaultdict(int)
        for point in all_points:
            point_frequencies[repr(point)] += 1
        all_points_conforming_to_threshold = list(
            filter(lambda k: k >= overlap_threshold,
                   point_frequencies.values()))
        return len(all_points_conforming_to_threshold)

    def get_basis_points_for_all_line_segments(self):
        return list(chain(*[i.basis_points()
                          for i in self.line_segments_filtered]))


def run_part_1(input: TextIOWrapper) -> None:
    hvas = HydrothermalVentsAvoidanceSystem(input)
    number_of_dangerous_points = hvas.calculate_dangerous_points()
    return number_of_dangerous_points
