# TODO(DP): use getters
class ScoreHolder:
    __LINE_SCORE_INCREMENT_MAPPING: dict[int, int] = {
        1: 100,
        2: 300,
        3: 700,
        4: 1500,
    }

    def __init__(self) -> None:
        self.__scores: int = 0
        self.__burned_line_count: int = 0

    def increment(self, burned_line_count: int) -> None:
        if burned_line_count not in self.__LINE_SCORE_INCREMENT_MAPPING:
            raise ValueError(f'Invalid burned_line_count [{burned_line_count}]!')

        score_increment = self.__LINE_SCORE_INCREMENT_MAPPING[burned_line_count]

        self.__scores += score_increment
        self.__burned_line_count += burned_line_count

    def get_score(self) -> int:
        return self.__scores

    def get_burned_line_count(self) -> int:
        return self.__burned_line_count
