from base_engine_event_handler import BaseEngineEventHandler
from engine_event import EngineEvent
from game_event import GameEvent


class TestEngineEventHandler(BaseEngineEventHandler):
    def handle(self, event: EngineEvent) -> GameEvent:
        # TODO(DP): --> extract draw logic
        self._stdscr.addstr(f'{event.name} ')
        self._stdscr.refresh()
        # TODO(DP): <-- extract draw logic

        return GameEvent.CONTINUE
