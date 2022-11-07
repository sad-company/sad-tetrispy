import curses

from engine import Engine
from test_engine_event_handler import TestEngineEventHandler


def main(stdscr) -> None:
    print("I am a cool game!")

    event_handler = TestEngineEventHandler(stdscr)
    engine = Engine(stdscr, event_handler, tick_duration_in_sec=1)

    engine.run()


if __name__ == '__main__':
    curses.wrapper(main)
