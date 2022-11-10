import unittest

from board import Board
from board_converter import BoardConverter
from point import Point


class BoardConverterTestCase(unittest.TestCase):
    def test_convert_to_string(self):
        board = Board(3, 4)
        points = [Point(1, 2), Point(1, 3), Point(2, 0), Point(2, 1), Point(2, 2), Point(2, 3)]
        board.set_cells_with_value(points, True)
        # ----
        # --xx
        # xxxx

        expected = '0 0 0 0\n' \
                   '0 0 1 1\n' \
                   '1 1 1 1\n'

        self.assertEqual(expected, BoardConverter.to_string(board))

    def test_convert_from_string_when_correct_cells_line(self):
        board_str = '0 0 0 0 0\n' \
                    '0 1 0 1 0\n' \
                    '0 0 0 0 0\n' \
                    '1 0 0 0 1\n' \
                    '0 1 1 1 0\n' \
                    '0 0 0 0 0\n'

        expected = Board(6, 5)
        points = [Point(1, 1), Point(1, 3),
                  Point(3, 0), Point(3, 4),
                  Point(4, 1), Point(4, 2),
                  Point(4, 3)]

        expected.set_cells_with_value(points, True)

        self.assertEqual(expected.get_cells(), BoardConverter.from_string(board_str).get_cells())

    def test_when_double_convertation(self):
        board_srt = '0 0 0 0 0\n' \
                    '0 1 0 1 0\n' \
                    '0 0 0 0 0\n' \
                    '1 0 0 0 1\n' \
                    '0 1 1 1 0\n' \
                    '0 0 0 0 0\n'

        board_from_str = BoardConverter.from_string(board_srt)
        board_from_str = BoardConverter.to_string(board_from_str)

        self.assertEqual(board_srt, board_from_str)
