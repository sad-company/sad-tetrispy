import unittest

from figure_factory import FigureFactory
from figure_kind import FigureKind
from figure_mover import FigureMover
from point import Point
from rotation_kind import RotationKind


class FigureMoverTestCase(unittest.TestCase):
    def test_when_rotate_figure(self):
        # NOTE: Set board_weight=2 to have figure at 0 position (not in the board center)
        line_figure = FigureFactory.create(FigureKind.LINE, 2)
        points = [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)]

        self.assertEqual(RotationKind.ROTATION_0, line_figure.rotation)
        self.assertEqual(points, line_figure.points)

        expected_new_points = [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]
        expected_rotation = RotationKind.ROTATION_90

        actual_points, actual_rotation = FigureMover.rotate(line_figure)

        self.assertEqual(expected_new_points, actual_points)
        self.assertEqual(expected_rotation, actual_rotation)

    def test_when_move_figure(self):
        snake_figure = FigureFactory.create(FigureKind.SNAKE_LEFT, 2)
        points = [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 2)]

        self.assertEqual(points, snake_figure.points)

        sub_tests_data = {
            'Move right': (FigureMover.move_right, [Point(0, 1), Point(0, 2), Point(1, 2), Point(1, 3)], Point(0, 1)),
            'Move left': (FigureMover.move_left, [Point(0, -1), Point(0, 0), Point(1, 0), Point(1, 1)], Point(0, -1)),
            'Move down': (FigureMover.move_down, [Point(1, 0), Point(1, 1), Point(2, 1), Point(2, 2)], Point(1, 0)),
        }

        for sub_test, (func, expected_points, expected_position) in sub_tests_data.items():
            with self.subTest(name=sub_test):
                actual_points, actual_position = func(snake_figure)
                self.assertEqual(actual_position, expected_position)
                self.assertEqual(actual_points, expected_points)
