from cells_type import CellsType


class Board:
    def __init__(self, height: int, weight: int) -> None:
        self.height = height
        self.weight = weight

        if self.height <= 0 or self.weight <= 0:
            raise ValueError(f"Board parameters are invalid "
                             f"[height=({self.height})][weight=({self.weight})]!")

        self.__cells: CellsType = \
            [[False for _ in range(0, self.weight)] for _ in range(0, self.height)]
