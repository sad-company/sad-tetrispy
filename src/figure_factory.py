from figure import Figure
from figure_kind import FigureKind
from figure_kind_randomizer import FigureKindRandomizer
from figure_mover import FigureMover
from point import Point
from rotation_kind import RotationKind


class FigureFactory:
    __kind_randomizer = FigureKindRandomizer()

    @staticmethod
    def create(kind: FigureKind, board_weight: int) -> Figure:
        start_rotation = RotationKind.ROTATION_0
        figure_points = FigureMover.get_points_after_rotation(kind, start_rotation)
        center_position = board_weight // 2 - 1

        return Figure(kind, Point(0, center_position), figure_points, start_rotation)

    @staticmethod
    def create_random(board_weight: int) -> Figure:
        random_kind = FigureFactory.__kind_randomizer.get_random()

        return FigureFactory.create(random_kind, board_weight)
