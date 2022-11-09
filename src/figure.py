from dataclasses import dataclass

from figure_kind import FigureKind
from point import Point, Points


@dataclass
class Figure:
    kind: FigureKind
    position: Point
    points: Points
