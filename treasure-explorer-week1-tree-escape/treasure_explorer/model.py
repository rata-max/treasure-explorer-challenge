from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Action(str, Enum):
    MOVE_UP = "MOVE_UP"
    MOVE_DOWN = "MOVE_DOWN"
    MOVE_LEFT = "MOVE_LEFT"
    MOVE_RIGHT = "MOVE_RIGHT"
    COLLECT = "COLLECT"


@dataclass(frozen=True)
class TreasureInfo:
    position: tuple[int, int]
    value: int | None
    collected: bool


@dataclass(frozen=True)
class ItemInfo:
    position: tuple[int, int]
    kind: str
    collected: bool


@dataclass(frozen=True)
class Observation:
    turn: int
    position: tuple[int, int]
    exit_position: tuple[int, int]
    energy: int
    grid: tuple[str, ...]
    treasures: tuple[TreasureInfo, ...]
    items: tuple[ItemInfo, ...] = ()
    has_key: bool = False
