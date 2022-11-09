import copy

from figure import Figure
from figure_kind import FigureKind
from point import Point


class FigureFactory:
    kind_figure_points_mapping: dict[FigureKind, list[Point]] = {
        FigureKind.SQUARE: [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)],
        FigureKind.LINE: [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)],
        FigureKind.SNAKE_RIGHT: [Point(0, 1), Point(0, 2), Point(1, 0), Point(1, 1)],
        FigureKind.SNAKE_LEFT: [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 2)],
        FigureKind.CORNER_RIGHT: [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)],
        FigureKind.CORNER_LEFT: [Point(0, 1), Point(1, 1), Point(2, 0), Point(2, 1)],
        FigureKind.T_LETTER: [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 1)],
    }

    @staticmethod
    def create(kind: FigureKind) -> Figure:
        figure_points = copy.deepcopy(FigureFactory.kind_figure_points_mapping[kind])
        return Figure(kind, Point(0, 0), figure_points)
