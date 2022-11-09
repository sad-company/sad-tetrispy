import curses
from time import time

from base_engine_event_handler import BaseEngineEventHandler
from engine_event import EngineEvent

NO_PRESSED_KEY = -1


# TODO(DP): color support
# TODO(DP): use pyee for events (https://pyee.readthedocs.io/en/latest/)
class Engine:
    # TODO(DP): validate tick_duration_in_sec value (should be positive)
    def __init__(self,
                 stdscr,  # for terminal window interactions
                 event_handler: BaseEngineEventHandler,
                 tick_duration_in_sec: int) -> None:
        self.__stdscr = stdscr
        self.__tick_duration_in_sec = tick_duration_in_sec
        self.__event_handler = event_handler

    def __init_screen(self) -> None:
        # NOTE: do not wait for input when calling getch
        self.__stdscr.nodelay(True)
        # NOTE: disable cursor
        curses.curs_set(False)

    def run(self) -> None:
        self.__init_screen()
        self.__event_handler.handle(EngineEvent.START)

        last_tick_timestamp = time()

        # TODO(DP): handle self.__event_handler.handle_engine_event() results
        # TODO(DP): handle GameEvent.END to stop
        while True:
            current_timestamp = time()
            time_delta = current_timestamp - last_tick_timestamp

            if time_delta > self.__tick_duration_in_sec:
                last_tick_timestamp = current_timestamp

                self.__event_handler.handle(EngineEvent.TIME_TICK)

            pressed_key = self.__stdscr.getch()

            if pressed_key == NO_PRESSED_KEY:
                continue

            # TODO(DP): cover all input keys
            # TODO(DP): key mapping support (extract map)
            if pressed_key == curses.KEY_LEFT:
                self.__event_handler.handle(EngineEvent.MOVE_LEFT)
            elif pressed_key == curses.KEY_RIGHT:
                self.__event_handler.handle(EngineEvent.MOVE_RIGHT)
            elif pressed_key == curses.KEY_DOWN:
                self.__event_handler.handle(EngineEvent.TIME_TICK)
