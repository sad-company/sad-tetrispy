from cells_type import CellsType
from figure import Figure
from point import Point, Points


class Board:
    def __init__(self, height: int, weight: int) -> None:
        self.height = height
        self.weight = weight

        if self.height <= 0 or self.weight <= 0:
            raise ValueError(f"Board parameters are invalid "
                             f"[height=({self.height})][weight=({self.weight})]!")

        self.__cells: CellsType = \
            [[False for _ in range(0, self.weight)] for _ in range(0, self.height)]

    def __get_indexes_for_remove(self) -> list[int]:
        result = []

        for index, line in enumerate(self.__cells):
            if False in line:
                continue

            result.append(index)

        return result

    def is_cell_empty(self, point: Point) -> bool:
        # NOTE: x - height, y - weight

        # if point out of bounds then return that cell is not empty
        if not point.is_in_board(self.height, self.weight):
            return False

        return self.__cells[point.x][point.y] is False

    def get_cells(self) -> CellsType:
        return self.__cells

    def is_cells_empty(self, points: Points) -> bool:
        for point in points:
            if not self.is_cell_empty(point):
                return False

        return True

    def set_cells_with_value(self, points: Points, value: bool) -> None:
        for point in points:
            if not point.is_in_board(self.height, self.weight):
                raise ValueError(f"{point} out of bounds!")

            self.__cells[point.x][point.y] = value

    def is_on_bottom(self, figure: Figure) -> bool:
        for point in figure.points:
            point_below = Point(point.x + 1, point.y)

            if not self.is_cell_empty(point_below):
                return True

        return False

    def remove_lines_if_needed(self) -> int:
        """
        Line should be removed if all line cells are True (are filled)

        :return - count of removed lines if any
        """

        indexes_for_remove = self.__get_indexes_for_remove()

        # NOTE: Remove from bottom to top
        for index in reversed(indexes_for_remove):
            del self.__cells[index]

        removed_lines = len(indexes_for_remove)
        empty_line = [[False] * self.weight]

        self.__cells = empty_line * removed_lines + self.__cells

        return removed_lines
