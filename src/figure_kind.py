from enum import Enum, auto


class FigureKind(Enum):
    SQUARE = auto()
    LINE = auto()
    SNAKE_RIGHT = auto()
    SNAKE_LEFT = auto()
    CORNER_RIGHT = auto()
    CORNER_LEFT = auto()
    T_LETTER = auto()
