from abc import ABC, abstractmethod
# from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        if cost <= 0:
            raise ValueError("cost must be positive")
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
