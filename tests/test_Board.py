import unittest

from board import Board
from figure_factory import FigureFactory
from figure_kind import FigureKind
from point import Point


class BoardTestCase(unittest.TestCase):
    def test_when_figure_is_not_on_bottom(self):
        line_figure = FigureFactory.create(FigureKind.LINE)

        board_with_empty_cells = Board(4, 4)
        # NOTE: x - figure cell; o - filled cell
        # xxxx
        # ----
        # ----
        # ----
        board_with_some_filled_cells = Board(3, 4)
        board_with_some_filled_cells.set_cells_with_value([Point(2, 0), Point(2, 1)], True)
        # xxxx
        # ----
        # oo--
        another_board_with_some_filled_cells = Board(3, 5)
        another_board_with_some_filled_cells.set_cells_with_value([Point(1, 4)], True)
        # xxxx-
        # ----o
        # -----

        sub_tests_data = {
            'All cells are empty': (line_figure, board_with_empty_cells),
            'Some cells are filled': (line_figure, board_with_some_filled_cells),
            'Cell below and right from figure is filled': (line_figure, another_board_with_some_filled_cells),
        }

        for sub_test, (figure, board) in sub_tests_data.items():
            with self.subTest(name=sub_test):
                self.assertFalse(board.is_on_bottom(figure))

    def test_when_figure_is_on_bottom(self):
        snake_figure = FigureFactory.create(FigureKind.SNAKE_LEFT)

        board_with_empty_cells = Board(2, 4)
        # xx--
        # -xx-
        board_with_some_filled_cells = Board(3, 4)
        board_with_some_filled_cells.set_cells_with_value([Point(2, 1), Point(2, 2)], True)
        # xx--
        # -xx-
        # -oo-
        another_board_with_some_filled_cells = Board(3, 4)
        another_board_with_some_filled_cells.set_cells_with_value([Point(1, 1)], True)
        # xx--
        # oxx-
        # ----

        sub_tests_data = {
            'All cells are empty, figure on bottom': (snake_figure, board_with_empty_cells),
            'Some cells are filled below whole figure': (snake_figure, board_with_some_filled_cells),
            'Cell below snake "head" is filled, another cells below are empty':
                (snake_figure, another_board_with_some_filled_cells),
        }

        for sub_test, (figure, board) in sub_tests_data.items():
            with self.subTest(name=sub_test):
                self.assertTrue(board.is_on_bottom(figure))


if __name__ == '__main__':
    unittest.main()
