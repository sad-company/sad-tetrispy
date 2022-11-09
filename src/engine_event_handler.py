from base_engine_event_handler import BaseEngineEventHandler
from board import Board
from engine_event import EngineEvent
from game_event import GameEvent
from point import Point
from renderer import Renderer
from score_holder import ScoreHolder

# TODO(DP): remove after figure generation integration
emulated_figure_cells = [
    Point(0, 5),
    Point(1, 6),
    Point(1, 5),
    Point(2, 6),
]


class EngineEventHandler(BaseEngineEventHandler):
    def __init__(self, stdscr, board: Board) -> None:
        super().__init__(stdscr, board)

        self.__renderer = Renderer(stdscr)
        self.__score_holder = ScoreHolder()

    def handle(self, event: EngineEvent) -> GameEvent:
        if not self._board.is_cells_empty(emulated_figure_cells):
            return GameEvent.END

        # TODO(DP): add "figure touches bottom" check

        # TODO(DP): use self.__score_holder

        # TODO(DP): --> replace after with FigureMover
        if event == EngineEvent.TIME_TICK:
            for cell in emulated_figure_cells:
                cell.x += 1

        if event == EngineEvent.MOVE_RIGHT:
            for cell in emulated_figure_cells:
                cell.y += 1

        if event == EngineEvent.MOVE_LEFT:
            for cell in emulated_figure_cells:
                cell.y -= 1
        # TODO(DP): <-- replace after with FigureMover
        self.__renderer.render(self._board,
                               emulated_figure_cells,
                               self.__score_holder)

        return GameEvent.CONTINUE
