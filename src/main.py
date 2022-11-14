import curses

from board import Board
from engine import Engine
from engine_event_handler import EngineEventHandler


def main(stdscr) -> None:
    board = Board(height=20, weight=10)
    event_handler = EngineEventHandler(stdscr,
                                       board,
                                       initial_ticks_for_move_down=50)
    engine = Engine(stdscr, event_handler, tick_duration_in_sec=0.02)

    engine.run()


if __name__ == '__main__':
    curses.wrapper(main)
