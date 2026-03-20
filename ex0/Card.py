from enum import IntEnum
from abc import ABC, abstractmethod


class Rarity(IntEnum):
    COMMON = 10
    UNCOMMON = 20
    RARE = 30
    LEGENDARY = 40


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
