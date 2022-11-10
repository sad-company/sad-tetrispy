import curses
from time import time

from base_engine_event_handler import BaseEngineEventHandler
from engine_event import EngineEvent
from game_event import GameEvent

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
        # TODO(DP): cover all input keys
        self.__key_engine_event_mapping: dict[int, EngineEvent] = {
            curses.KEY_LEFT: EngineEvent.MOVE_LEFT,
            curses.KEY_RIGHT: EngineEvent.MOVE_RIGHT,
            curses.KEY_DOWN: EngineEvent.TIME_TICK,
        }
        self.__last_tick_timestamp = time()

    def __init_screen(self) -> None:
        # NOTE: do not wait for input when calling getch
        self.__stdscr.nodelay(True)
        # NOTE: disable cursor
        curses.curs_set(False)

    def __is_tick_time(self) -> bool:
        current_timestamp = time()
        time_delta = current_timestamp - self.__last_tick_timestamp

        if time_delta < self.__tick_duration_in_sec:
            return False

        self.__last_tick_timestamp = current_timestamp

        return True

    def __try_get_engine_event_by_input_key(self) -> EngineEvent | None:
        pressed_key = self.__stdscr.getch()

        if pressed_key == NO_PRESSED_KEY:
            return None

        return self.__key_engine_event_mapping.get(pressed_key)

    def __get_engine_events(self) -> list[EngineEvent]:
        result = []

        if self.__is_tick_time():
            result.append(EngineEvent.TIME_TICK)

        engine_event = self.__try_get_engine_event_by_input_key()

        if engine_event is not None:
            result.append(engine_event)

        return result

    def run(self) -> None:
        self.__init_screen()
        self.__event_handler.handle(EngineEvent.START)

        # TODO(DP): handle self.__event_handler.handle_engine_event() results
        # TODO(DP): handle GameEvent.END to stop
        while True:
            for engine_event in self.__get_engine_events():
                game_event = self.__event_handler.handle(engine_event)

                if game_event == GameEvent.END:
                    break
