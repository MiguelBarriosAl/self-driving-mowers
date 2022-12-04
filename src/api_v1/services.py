from api_v1.checkers import check_coord
from api_v1.logs import Logs

logs = Logs()


def movements(top: list, position: list, instructions: str) -> list:
    cardinal_points = ["W", "N", "E", "S"]
    X = position[0]
    Y = position[1]
    coord = position[2]
    cardinal_index = cardinal_points.index(coord)
    instruction = Instruccions(X, Y, cardinal_index)
    for i in instructions:

        if "L" in i:
            X, Y, coord = instruction.left()
            logs.info(X, Y, cardinal_points[coord])

        elif "R" in i:
            X, Y, coord = instruction.right()
            logs.info(X, Y, cardinal_points[coord])

        elif "M" in i:
            X, Y, coord = instruction.moving()
            logs.info(X, Y, cardinal_points[coord])
        else:
            logs.mov_error(i)
    check_coord(top, [X, Y, coord])
    output = [X, Y, cardinal_points[coord]]
    return output


class Instruccions:
    """
        C = [West, North, East, South]
        If mower rotates, its orientation is updated.
        f mower moves forward, a position is added with respect to its orientation
            West -> X = X - 1
            North -> Y = Y + 1
            East -> X = X + 1
            South -> X = Y - 1
    """

    def __init__(self, X: int, Y: int, index: int):
        self.x = X
        self.y = Y
        self.index = index

    def left(self):
        if self.index > 0:
            self.index -= 1
        elif self.index == 0:
            self.index = 3
        return self.x, self.y, self.index

    def right(self):
        if self.index < 3:
            self.index += 1
        elif self.index == 3:
            self.index = 0
        return self.x, self.y, self.index

    def moving(self):
        if self.index == 0:
            self.x -= 1
        elif self.index == 1:
            self.y += 1
        elif self.index == 2:
            self.x += 1
        elif self.index == 3:
            self.y -= 1
        return self.x, self.y, self.index
