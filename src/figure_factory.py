import copy

from figure import Figure
from figure_kind import FigureKind
from figure_mover import FigureMover
from point import Point
from rotation_kind import RotationKind


class FigureFactory:
    @staticmethod
    def create(kind: FigureKind) -> Figure:
        start_rotation = RotationKind.ROTATION_0
        figure_points = copy.deepcopy(
            FigureMover.rotation_figure_points_mapping[start_rotation][kind])

        return Figure(kind, Point(0, 0), figure_points, start_rotation)
