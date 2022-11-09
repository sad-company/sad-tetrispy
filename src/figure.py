from dataclasses import dataclass

from figure_kind import FigureKind
from point import Point


@dataclass
class Figure:
    kind: FigureKind
    position: Point
    points: list[Point]
