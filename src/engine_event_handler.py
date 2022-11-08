from base_engine_event_handler import BaseEngineEventHandler
from board import Board
from engine_event import EngineEvent
from game_event import GameEvent
from point import Point
from renderer import Renderer

# TODO(DP): remove after figure generation integration
emulated_figure_cells = [
    Point(0, 5),
    Point(1, 6),
    Point(1, 5),
    Point(2, 6),
]


class EngineEventHandler(BaseEngineEventHandler):
    def __init__(self, stdscr, board: Board):
        super().__init__(stdscr, board)

        self.__renderer = Renderer(stdscr)

    def handle(self, event: EngineEvent) -> GameEvent:
        # TODO(DP): add "figure touches bottom" check

        # TODO(DP): --> remove after figure generation integration
        if event == EngineEvent.TIME_TICK:
            for cell in emulated_figure_cells:
                cell.x += 1
        # TODO(DP): <-- remove after figure generation integration
        self.__renderer.render(self._board, emulated_figure_cells)

        return GameEvent.CONTINUE
