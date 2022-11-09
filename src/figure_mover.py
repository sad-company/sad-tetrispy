from figure import Figure
from point import Point, Points

NewPoints = Points


class FigureMover:
    @staticmethod
    def move_right(figure: Figure) -> NewPoints:
        new_points: NewPoints = []

        for point in figure.points:
            new_points.append(Point(point.x, point.y + 1))

        return new_points

    @staticmethod
    def move_left(figure: Figure) -> NewPoints:
        new_points: NewPoints = []

        for point in figure.points:
            new_points.append(Point(point.x, point.y - 1))

        return new_points

    @staticmethod
    def rotate(figure: Figure) -> NewPoints:
        raise NotImplementedError("Please wait a minute (or day :))")
