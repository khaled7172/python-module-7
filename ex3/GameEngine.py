from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Optional


class GameEngine:
    def __init__(self):
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns = 0
        self.total_damage = 0
        self.hand = []

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            factory.create_creature("dragon"),
            factory.create_creature("goblin"),
            factory.create_spell("fireball")
        ]

    def simulate_turn(self) -> dict:
        if not self.strategy or not self.factory:
            raise RuntimeError("Engine not configured")
        self.turns += 1
        result = self.strategy.execute_turn(self.hand, ["Enemy Player"])
        self.total_damage += result["damage_dealt"]
        return result

    def get_engine_status(self) -> dict:
        if not self.strategy:
            raise RuntimeError("Engine not configured")
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": len(self.hand)
        }
