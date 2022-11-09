import random

from figure_kind import FigureKind


class FigureKindRandomizer:
    def __init__(self) -> None:
        self.__kinds = list(FigureKind)

    def random(self) -> FigureKind:
        return random.choice(self.__kinds)
