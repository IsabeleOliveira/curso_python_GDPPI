from enum import Enum


class Directions(Enum):
    right = 0
    left = 1


def movimento(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')


    return f'Movendo {direction.name}'


if __name__ == "__main__":
    print(movimento(Directions.right))
    print(movimento(Directions.left))

