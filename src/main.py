import curses

from board import Board
from engine import Engine
from engine_event_handler import EngineEventHandler
from point import Point


def main(stdscr) -> None:
    board = Board(20, 10)
    # TODO(DP): --> remove after test
    prefilled_points = [Point(board.height - 1, i) for i in range(5)]

    board.set_cells_with_value(prefilled_points, True)
    # TODO(DP): <-- remove after test

    event_handler = EngineEventHandler(stdscr, board)
    engine = Engine(stdscr, event_handler, tick_duration_in_sec=1)

    engine.run()


if __name__ == '__main__':
    curses.wrapper(main)
