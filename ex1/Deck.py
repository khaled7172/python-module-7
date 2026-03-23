# from typing import Dict
import random
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


class Deck():
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Deck is empty")
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(
                self.cards), "creatures": sum(
                1 for c in self.cards if isinstance(
                    c, CreatureCard)), "spells": sum(
                    1 for c in self.cards if isinstance(
                        c, SpellCard)), "artifacts": sum(
                            1 for c in self.cards if isinstance(
                                c, ArtifactCard)), "avg_cost": sum(
                                    c.cost for c in self.cards) / len(
                                        self.cards) if self.cards else 0.0}
