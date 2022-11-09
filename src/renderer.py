import curses.textpad

from board import Board


class Renderer:
    __BORDER_WEIGHT: int = 1
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

    def __draw_board_cells(self, board: Board) -> None:
        board_cells = board.get_cells()

        for x in range(board.height):
            for y in range(board.weight):
                is_cell_fill = board_cells[x][y]

                self.__draw_cell(x, y, is_cell_fill)

    # TODO(DP): use Figure class instead of figure_points
    def __draw_figure(self, figure_points: list) -> None:
        for point in figure_points:
            self.__draw_cell(point.x, point.y, is_fill=True)

    # TODO(DP): use Figure class instead of figure_points
    def render(self, board: Board, figure_points: list) -> None:
        self.__before_render()
        self.__draw_board_border(board)
        self.__draw_board_cells(board)
        self.__draw_figure(figure_points)
