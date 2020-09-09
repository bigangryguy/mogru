from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar('T', bound='Entity')


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self,
                 x: int = 0, y: int = 0,
                 char: str = '?',
                 color: Tuple[int, int, int] = (255, 255, 255),
                 name: str = '<Unnamed>',
                 blocks_movement: bool = False):
        self.x: int = x
        self.y: int = y
        self.char: str = char
        self.color: Tuple[int, int, int] = color
        self.name: str = name
        self.blocks_movement: bool = blocks_movement

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location.
        """
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone

    def move(self, dx: int, dy: int) -> None:
        """Move the entity the specified amount.
        """
        self.x += dx
        self.y += dy
