from cells_type import CellsType
from point import Point


class Board:
    def __init__(self, height: int, weight: int) -> None:
        self.height = height
        self.weight = weight

        if self.height <= 0 or self.weight <= 0:
            raise ValueError(f"Board parameters are invalid "
                             f"[height=({self.height})][weight=({self.weight})]!")

        self.__cells: CellsType = \
            [[False for _ in range(0, self.weight)] for _ in range(0, self.height)]

    def is_cell_empty(self, point: Point) -> bool:
        # NOTE: x - height, y - weight

        # if point out of bounds then return that cell is not empty
        if not point.is_in_board(self.height, self.weight):
            return False

        return self.__cells[point.x][point.y] is False

    def get_cells(self) -> CellsType:
        return self.__cells

    def is_cells_empty(self, points: list[Point]) -> bool:
        for point in points:
            if not self.is_cell_empty(point):
                return False

        return True

    def set_cells_with_value(self, points: list[Point], value: bool) -> None:
        for point in points:
            if not point.is_in_board(self.height, self.weight):
                raise ValueError(f"{point} out of bounds!")

            self.__cells[point.x][point.y] = value
