from base_engine_event_handler import BaseEngineEventHandler
from board import Board
from engine_event import EngineEvent
from figure_factory import FigureFactory
from game_event import GameEvent
from renderer import Renderer
from score_holder import ScoreHolder


class EngineEventHandler(BaseEngineEventHandler):
    def __init__(self, stdscr, board: Board) -> None:
        super().__init__(stdscr, board)

        self.__renderer = Renderer(stdscr)
        self.__score_holder = ScoreHolder()
        self.__current_figure = FigureFactory.create_random()
        self.__next_figure = FigureFactory.create_random()

    def __use_next_figure(self) -> None:
        self.__current_figure = self.__next_figure
        self.__next_figure = FigureFactory.create_random()

    def handle(self, event: EngineEvent) -> GameEvent:
        current_figure_points = self.__current_figure.points

        if not self._board.is_cells_empty(current_figure_points):
            return GameEvent.END

        # TODO(DP): add "figure touches bottom" check

        # TODO(DP): use __use_next_figure()

        # TODO(DP): use self.__score_holder

        # TODO(DP): --> replace after with FigureMover
        if event == EngineEvent.TIME_TICK:
            for cell in current_figure_points:
                cell.x += 1

        if event == EngineEvent.MOVE_RIGHT:
            for cell in current_figure_points:
                cell.y += 1

        if event == EngineEvent.MOVE_LEFT:
            for cell in current_figure_points:
                cell.y -= 1
        # TODO(DP): <-- replace after with FigureMover
        self.__renderer.render(self._board,
                               current_figure_points,
                               self.__next_figure,
                               self.__score_holder)

        return GameEvent.CONTINUE
