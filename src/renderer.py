import curses.textpad

from board import Board
from figure import Figure
from point import Point
from score_holder import ScoreHolder


class Renderer:
    __BORDER_WEIGHT: int = 1
    __NEXT_FIGURE_TOP_PADDING: int = 1
    __STATISTIC_TOP_PADDING: int = 7
    __STATISTIC_BLOCKS_PADDING: int = 2
    __CELL_CHARACTER: dict[bool, str] = {
        True: '▨',
        False: ' ',
    }

    def __init__(self, stdscr) -> None:
        self.__stdscr = stdscr

    def __before_render(self) -> None:
        self.__stdscr.clear()

    def __draw_board_border(self, board: Board) -> None:
        curses.textpad.rectangle(self.__stdscr,
                                 0,
                                 0,
                                 board.height + self.__BORDER_WEIGHT,
                                 board.weight + self.__BORDER_WEIGHT)

    def __draw_cell(self, x: int, y: int, is_fill: bool) -> None:
        self.__stdscr.addch(x + self.__BORDER_WEIGHT,
                            y + self.__BORDER_WEIGHT,
                            self.__CELL_CHARACTER[is_fill])

    def __draw_string(self, x: int, y: int, value: str) -> None:
        self.__stdscr.addstr(x, y, value)

    def __draw_board_cells(self, board: Board) -> None:
        board_cells = board.get_cells()

        for x in range(board.height):
            for y in range(board.weight):
                is_cell_fill = board_cells[x][y]

                self.__draw_cell(x, y, is_cell_fill)

    def __draw_figure(self, figure_points: list[Point]) -> None:
        for point in figure_points:
            self.__draw_cell(point.x, point.y, is_fill=True)

    def __get_y_outside_board(self, board: Board) -> int:
        return board.weight + self.__BORDER_WEIGHT + 1

    def __draw_next_figure(self, board: Board, figure: Figure) -> None:
        x = self.__NEXT_FIGURE_TOP_PADDING
        y = self.__get_y_outside_board(board)

        self.__draw_string(x, y, 'Next:')
        x += 1

        next_figure_points = [
            Point(point.x + x, point.y + y) for point in figure.points]

        self.__draw_figure(next_figure_points)

    def __draw_statistic(self, board: Board, score_holder: ScoreHolder) -> None:
        x = self.__STATISTIC_TOP_PADDING
        y = self.__get_y_outside_board(board)

        self.__draw_string(x, y, 'Scores:')
        x += 1

        self.__draw_string(x, y, str(score_holder.get_scores()))
        x += self.__STATISTIC_BLOCKS_PADDING

        self.__draw_string(x, y, 'Lines:')
        x += 1

        self.__draw_string(x, y, str(score_holder.get_burned_line_count()))

    def __show_logs(self, log_lines: list[str]) -> None:
        y = 0
        x = 25

        self.__draw_string(y, x, 'Logs:')

        for i, log_line in enumerate(log_lines[-20:]):
            self.__draw_string(y + i + 1, 25, log_line)

    def render(self, board: Board, figure: Figure,
               next_figure: Figure, score_holder: ScoreHolder,
               log_lines: list[str]) -> None:
        self.__before_render()
        self.__draw_board_border(board)
        self.__draw_next_figure(board, next_figure)
        self.__draw_statistic(board, score_holder)
        self.__draw_board_cells(board)
        self.__draw_figure(figure.get_points())

        if len(log_lines) > 0:
            self.__show_logs(log_lines)
