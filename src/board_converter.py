from board import Board
from point import Point, Points


class BoardConverter:
    @staticmethod
    def to_string(board: Board) -> str:
        result = ''

        for line in board.get_cells():
            for cell in line:
                result += '1 ' if cell else '0 '

            result = result.rstrip(' ')
            result += '\n'

        return result

    @staticmethod
    def from_string(value: str) -> Board:
        lines: list[list[str]] = [line.split(' ')
                                  for line in value.split('\n')
                                  if len(line) > 0]
        height = len(lines)
        weight = len(lines[0])
        board = Board(height, weight)
        points: Points = []

        for x, line in enumerate(lines):
            for y, cell in enumerate(line):
                if cell == '1':
                    points.append(Point(x, y))

        board.set_cells_with_value(points, True)

        return board
