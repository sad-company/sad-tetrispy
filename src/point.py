from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x,
                     self.y + other.y)

    def is_in_board(self, height: int, weight: int) -> bool:
        is_x_in_bounds = 0 <= self.x < height
        is_y_in_bounds = 0 <= self.y < weight

        return is_x_in_bounds and is_y_in_bounds


Points = list[Point]
