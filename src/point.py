from dataclasses import dataclass
from typing import Tuple

PointType = Tuple[int, int]


@dataclass
class Point:
    x: int
    y: int
