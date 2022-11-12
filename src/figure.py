from dataclasses import dataclass

from figure_kind import FigureKind
from point import Point, Points
from rotation_kind import RotationKind


@dataclass
class Figure:
    kind: FigureKind
    position: Point
    points: Points
    rotation: RotationKind

    def get_points(self) -> Points:
        return self.position.add_to(self.points)
