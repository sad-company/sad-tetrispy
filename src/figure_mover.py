import copy
from typing import Tuple

from figure import Figure
from figure_kind import FigureKind
from point import Point, Points
from rotation_kind import RotationKind

NewPoints = Points
NewRotation = RotationKind
RotationResult = Tuple[NewPoints, NewRotation]


class FigureMover:
    __kind_rotation_points_mapping: dict[FigureKind, dict[RotationKind, Points]] = {
        FigureKind.SQUARE:
            {
                RotationKind.ROTATION_0: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
                RotationKind.ROTATION_90: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
                RotationKind.ROTATION_180: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
                RotationKind.ROTATION_270: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
            },
        FigureKind.LINE:
            {
                RotationKind.ROTATION_0: [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)],
                RotationKind.ROTATION_90: [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)],
                RotationKind.ROTATION_180: [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)],
                RotationKind.ROTATION_270: [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)],
            },
        FigureKind.SNAKE_RIGHT:
            {
                RotationKind.ROTATION_0: [Point(0, 1), Point(0, 2), Point(1, 0), Point(1, 1)],
                RotationKind.ROTATION_90: [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)],
                RotationKind.ROTATION_180: [Point(0, 1), Point(0, 2), Point(1, 0), Point(1, 1)],
                RotationKind.ROTATION_270: [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)],
            },
        FigureKind.SNAKE_LEFT:
            {
                RotationKind.ROTATION_0: [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 2)],
                RotationKind.ROTATION_90: [Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 0)],
                RotationKind.ROTATION_180: [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 2)],
                RotationKind.ROTATION_270: [Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 0)],
            },
        FigureKind.CORNER_RIGHT:
            {
                RotationKind.ROTATION_0: [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)],
                RotationKind.ROTATION_90: [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 0)],
                RotationKind.ROTATION_180: [Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1)],
                RotationKind.ROTATION_270: [Point(1, 0), Point(1, 1), Point(1, 2), Point(0, 2)],
            },
        FigureKind.CORNER_LEFT:
            {
                RotationKind.ROTATION_0: [Point(0, 1), Point(1, 1), Point(2, 0), Point(2, 1)],
                RotationKind.ROTATION_90: [Point(1, 0), Point(1, 1), Point(1, 2), Point(0, 2)],
                RotationKind.ROTATION_180: [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)],
                RotationKind.ROTATION_270: [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 0)],
            },
        FigureKind.T_LETTER:
            {
                RotationKind.ROTATION_0: [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 1)],
                RotationKind.ROTATION_90: [Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 1)],
                RotationKind.ROTATION_180: [Point(0, 1), Point(1, 0), Point(1, 1), Point(1, 2)],
                RotationKind.ROTATION_270: [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 0)],
            },
    }

    @staticmethod
    def get_points_after_rotation(kind: FigureKind, rotation: RotationKind) -> NewPoints:
        return copy.deepcopy(FigureMover.__kind_rotation_points_mapping[kind][rotation])

    @staticmethod
    def rotate(figure: Figure) -> RotationResult:
        """Clockwise rotation of figure based on its type"""
        new_rotation = figure.rotation.get_next()
        new_points = FigureMover.get_points_after_rotation(figure.kind, new_rotation)

        return new_points, new_rotation

    @staticmethod
    def __move(figure: Figure, move_point: Point) -> NewPoints:
        new_points: NewPoints = []

        for point in figure.points:
            new_points.append(Point(point.x + move_point.x, point.y + move_point.y))

        return new_points

    @staticmethod
    def move_right(figure: Figure) -> NewPoints:
        return FigureMover.__move(figure, Point(0, 1))

    @staticmethod
    def move_left(figure: Figure) -> NewPoints:
        return FigureMover.__move(figure, Point(0, -1))

    @staticmethod
    def move_down(figure: Figure) -> NewPoints:
        return FigureMover.__move(figure, Point(1, 0))
