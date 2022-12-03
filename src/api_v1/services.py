from api_v1.checkers import check_coord
from api_v1.logs import Logs

logs = Logs()


def movements(top, position, instructions):
    cardinal_points = ["0", "N", "E", "S"]
    X = position[0]  # type: int
    Y = position[1]  # type: int
    coord = position[2]  # type: str
    cardinal_index = cardinal_points.index(coord)
    instruction = Instruccions(X, Y, cardinal_index)
    for i in instructions:

        if "L" in i:
            X, Y, coord = instruction.left()
            print("Is L: ", X, Y, cardinal_points[coord])
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
