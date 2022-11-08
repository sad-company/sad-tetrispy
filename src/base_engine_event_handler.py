from abc import ABC, abstractmethod

from board import Board
from engine_event import EngineEvent
from game_event import GameEvent


class BaseEngineEventHandler(ABC):
    def __init__(self, stdscr, board: Board):
        self._stdscr = stdscr
        self._board = board

    @abstractmethod
    def handle(self, event: EngineEvent) -> GameEvent:
        pass
