from io import TextIOWrapper
from itertools import chain
from typing import Literal, List, Self
from .part_1 import HydrothermalVentsAvoidanceSystem, LineSegment, Point


class LineSegmentImproved(LineSegment):
    direction: Literal["VERTICAL", "HORIZONTAL", "DIAGONAL"]

    @staticmethod
    def from_str(s: str) -> Self:
        """
        Create a LineSegment instance from a text like "x1,y1 -> x2,y2"
        """
        points = s.split(" -> ")
        assert len(points) == 2
        start = Point.from_str(points[0])
        end = Point.from_str(points[1])
        line_segment = LineSegmentImproved(start, end)
        return line_segment

    def get_direction(self) -> Literal["VERTICAL", "HORIZONTAL", "DIAGONAL"]:
        if self.start.x == self.end.x:
            return "VERTICAL"
        elif self.start.y == self.end.y:
            return "HORIZONTAL"
        else:
            return "DIAGONAL"
        return "VERTICAL" if self.start.x == self.end.x else "HORIZONTAL"

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
        elif self.direction == "HORIZONTAL":
            # horizontal line
            sorted_axis = sorted([self.start.x, self.end.x])
            for i in range(sorted_axis[0], sorted_axis[1] + 1):
                basis_point = Point(i, self.start.y)
                points.append(basis_point)
        else:
            # take difference b/w any axis, let's use X axis
            x_value_difference = abs(self.start.x - self.end.x)
            for i in range(0, x_value_difference + 1):
                x_value = self.start.x + i if self.start.x < self.end.x else self.start.x - i
                y_value = self.start.y + i if self.start.y < self.end.y else self.start.y - i
                basis_point = Point(x_value, y_value)
                points.append(basis_point)
        return points


class HVASImproved(HydrothermalVentsAvoidanceSystem):
    # all line segments from input
    line_segments: List[LineSegmentImproved]

    def __init__(self, input: TextIOWrapper):
        line_segments_raw = list(
            filter(lambda k: k != "", input.read().split("\n")))
        self.line_segments = [LineSegmentImproved.from_str(
            i) for i in line_segments_raw]

    def get_basis_points_for_all_line_segments(self):
        return list(chain(*[i.basis_points()
                          for i in self.line_segments]))


def run_part_2(input: TextIOWrapper):
    hvas = HVASImproved(input)
    number_of_dangerous_points = hvas.calculate_dangerous_points()
    return number_of_dangerous_points
