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
    rotation_figure_points_mapping: dict[RotationKind, dict[FigureKind, Points]] = {
        RotationKind.ROTATION_0:
            {
                FigureKind.SQUARE: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
                FigureKind.LINE: [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)],
                FigureKind.SNAKE_RIGHT: [Point(0, 1), Point(0, 2), Point(1, 0), Point(1, 1)],
                FigureKind.SNAKE_LEFT: [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 2)],
                FigureKind.CORNER_RIGHT: [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)],
                FigureKind.CORNER_LEFT: [Point(0, 1), Point(1, 1), Point(2, 0), Point(2, 1)],
                FigureKind.T_LETTER: [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 1)],
            },
        RotationKind.ROTATION_90:
            {
                FigureKind.SQUARE: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
                FigureKind.LINE: [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)],
                FigureKind.SNAKE_RIGHT: [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)],
                FigureKind.SNAKE_LEFT: [Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 0)],
                FigureKind.CORNER_RIGHT: [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 0)],
                FigureKind.CORNER_LEFT: [Point(1, 0), Point(1, 1), Point(1, 2), Point(0, 2)],
                FigureKind.T_LETTER: [Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 1)],
            },
        RotationKind.ROTATION_180:
            {
                FigureKind.SQUARE: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
                FigureKind.LINE: [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)],
                FigureKind.SNAKE_RIGHT: [Point(0, 1), Point(0, 2), Point(1, 0), Point(1, 1)],
                FigureKind.SNAKE_LEFT: [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 2)],
                FigureKind.CORNER_RIGHT: [Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1)],
                FigureKind.CORNER_LEFT: [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)],
                FigureKind.T_LETTER: [Point(0, 1), Point(1, 0), Point(1, 1), Point(1, 2)],
            },
        RotationKind.ROTATION_270:
            {
                FigureKind.SQUARE: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
                FigureKind.LINE: [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)],
                FigureKind.SNAKE_RIGHT: [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)],
                FigureKind.SNAKE_LEFT: [Point(0, 1), Point(1, 0), Point(1, 1), Point(2, 0)],
                FigureKind.CORNER_RIGHT: [Point(1, 0), Point(1, 1), Point(1, 2), Point(0, 2)],
                FigureKind.CORNER_LEFT: [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 0)],
                FigureKind.T_LETTER: [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 0)],
            }
    }

    @staticmethod
    def rotate(figure: Figure) -> RotationResult:
        """Clockwise rotation of figure based on its type"""
        new_rotation = figure.rotation.get_next()
        new_points = copy.deepcopy(
            FigureMover.rotation_figure_points_mapping[new_rotation][figure.kind])

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
