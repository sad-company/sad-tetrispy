from board import Board


class BoardConverter:

    @staticmethod
    def to_string(board: Board) -> str:
        result = ''

        for line in board.get_cells():
            for cell in line:
                result += '1 ' if cell else '0 '

            result += '\n'

        return result

    @staticmethod
    def from_string(value: str) -> Board:
        pass
