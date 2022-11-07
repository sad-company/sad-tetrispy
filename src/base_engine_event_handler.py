from abc import ABC, abstractmethod

from engine_event import EngineEvent
from game_event import GameEvent


class BaseEngineEventHandler(ABC):
    def __init__(self, stdscr):
        self._stdscr = stdscr

    @abstractmethod
    def handle(self, event: EngineEvent) -> GameEvent:
        pass
