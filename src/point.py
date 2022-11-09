from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def is_in_board(self, height: int, weight: int) -> bool:
        return self.x <= height \
               or self.y <= weight \
               or self.x > 0 \
               or self.y > 0
