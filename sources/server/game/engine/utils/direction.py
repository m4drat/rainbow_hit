import enum
import random

from server.game.engine.utils.point import Point


class Direction(enum.Enum):
    '''
    Describes all possible directions.
    '''
    North = N = Up = Point(0, 1)
    NorthEast = NE = RightUp = UpRight = Point(1, 1)
    East = E = Right = Point(1, 0)
    SouthEast = SE = DownRight = RightDown = Point(1, -1)
    South = S = Down = Point(0, -1)
    SouthWest = SW = LeftDown = DownLeft = Point(-1, -1)
    West = W = Left = Point(-1, 0)
    NorthWest = NW = LeftUp = UpLeft = Point(-1, 1)

    @staticmethod
    def rand_dir():
        return random.choice(list(Direction))

    # overloading '~' operator
    def __invert__(self):
        '''Inverts direction
        
        Returns
        -------
        dir : Direction

        Examples
        --------
        >>> ~Direction.Up
        <Direction.South: 5>
        
        '''
        if self == self.N:
            return self.S
        elif self == self.NE:
            return self.SW
        elif self == self.E:
            return self.W
        elif self == self.SE:
            return self.NW
        elif self == self.S:
            return self.N
        elif self == self.SW:
            return self.NE
        elif self == self.W:
            return self.E
        elif self == self.NW:
            return self.SE


'''    def __repr__(self):
        return self._value_'''
