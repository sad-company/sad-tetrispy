from enum import Enum


class RotationKind(Enum):
    ROTATION_0 = 1
    ROTATION_90 = 2
    ROTATION_180 = 3
    ROTATION_270 = 4

    def get_next(self) -> 'RotationKind':
        value = self.value + 1
        if value > 4:
            return RotationKind.ROTATION_0

        return RotationKind(value)

    def get_prev(self) -> 'RotationKind':
        value = self.value - 1
        if value == 0:
            return RotationKind.ROTATION_270

        return RotationKind(value)
