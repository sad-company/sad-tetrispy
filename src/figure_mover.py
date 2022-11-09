from figure import Figure
from point import Points

NewPoints = Points


class FigureMover:
    @staticmethod
    def move_right(figure: Figure) -> NewPoints:
        raise NotImplementedError("Ooops")

    @staticmethod
    def move_left(figure: Figure) -> NewPoints:
        raise NotImplementedError("Too early")

    @staticmethod
    def rotate(figure: Figure) -> NewPoints:
        raise NotImplementedError("Please wait a minute (or day :))")
