from enum import Enum, auto


class EngineEvent(Enum):
    # General
    START = auto()
    TIME_TICK = auto()
    # Interaction
    MOVE_LEFT = auto()
    MOVE_RIGHT = auto()
    ROTATE_CLOCKWISE = auto()
    # State
    PAUSE = auto()
    EXIT = auto()
