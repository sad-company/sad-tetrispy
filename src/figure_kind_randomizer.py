import random

from figure_kind import FigureKind


class FigureKindRandomizer:
    __kinds = list(FigureKind)

    @staticmethod
    def get_random() -> FigureKind:
        return random.choice(FigureKindRandomizer.__kinds)
