from figure import Figure
from figure_kind import FigureKind
from figure_kind_randomizer import FigureKindRandomizer
from figure_mover import FigureMover
from point import Point
from rotation_kind import RotationKind


class FigureFactory:
    __kind_randomizer = FigureKindRandomizer()

    @staticmethod
    def create(kind: FigureKind) -> Figure:
        start_rotation = RotationKind.ROTATION_0
        figure_points = FigureMover.get_points_after_rotation(kind, start_rotation)

        return Figure(kind, Point(0, 0), figure_points, start_rotation)

    @staticmethod
    def create_random() -> Figure:
        random_kind = FigureFactory.__kind_randomizer.get_random()

        return FigureFactory.create(random_kind)
