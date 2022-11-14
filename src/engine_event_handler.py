from base_engine_event_handler import BaseEngineEventHandler
from board import Board
from engine_event import EngineEvent
from figure_factory import FigureFactory
from figure_mover import FigureMover
from game_event import GameEvent
from renderer import Renderer
from score_holder import ScoreHolder


class EngineEventHandler(BaseEngineEventHandler):
    def __init__(self, stdscr, board: Board) -> None:
        super().__init__(stdscr, board)

        self.__renderer = Renderer(stdscr)
        self.__score_holder = ScoreHolder()
        self.__current_figure = FigureFactory.create_random(self._board.weight)
        self.__next_figure = FigureFactory.create_random(self._board.weight)

    def __use_next_figure(self) -> None:
        self.__current_figure = self.__next_figure
        self.__next_figure = FigureFactory.create_random(self._board.weight)

    def __is_game_end(self) -> bool:
        return not self._board.is_cells_empty(self.__current_figure.points)

    def handle(self, event: EngineEvent) -> GameEvent:
        if self.__is_game_end():
            return GameEvent.END

        if event == EngineEvent.TIME_TICK:
            new_points, new_position = FigureMover.move_down(self.__current_figure)

            if self._board.is_cells_empty(new_points):
                self.__current_figure.position = new_position
            else:
                self._board.set_cells_with_value(self.__current_figure.get_points(), True)

                removed_lines = self._board.remove_lines_if_needed()

                if removed_lines > 0:
                    self.__score_holder.increment(removed_lines)

                self.__use_next_figure()

        elif event == EngineEvent.MOVE_RIGHT:
            new_points, new_position = FigureMover.move_right(self.__current_figure)

            if self._board.is_cells_empty(new_points):
                self.__current_figure.position = new_position

        elif event == EngineEvent.MOVE_LEFT:
            new_points, new_position = FigureMover.move_left(self.__current_figure)

            if self._board.is_cells_empty(new_points):
                self.__current_figure.position = new_position

        elif event == EngineEvent.ROTATE_CLOCKWISE:
            new_points, new_rotation = FigureMover.rotate(self.__current_figure)
            points_for_check = self.__current_figure.position.add_to(new_points)

            if self._board.is_cells_empty(points_for_check):
                self.__current_figure.points = new_points
                self.__current_figure.rotation = new_rotation

        self.__renderer.render(self._board,
                               self.__current_figure,
                               self.__next_figure,
                               self.__score_holder)

        return GameEvent.CONTINUE
