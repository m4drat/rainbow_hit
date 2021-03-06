from typing import Union

from ..engine.utils.direction import Direction
from ..engine.utils.point import Point


class BotActivityDummy:
    def sleep(self):
        ...

    def step(self, direction: Direction):
        ...

    def shoot(self, obj: Union[Point, object]):
        ...

    def scan(self):
        ...

    def current_location(self) -> Point:
        ...

    def current_hp(self) -> int:
        ...

    @property
    def name(self):
        ...
