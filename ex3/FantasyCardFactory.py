from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int |
                        None = None) -> CreatureCard:
        creatures = {
            "dragon": CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
            "goblin": CreatureCard("Goblin Warrior", 2, "Common", 2, 1),
        }
        if isinstance(name_or_power, str):
            return creatures.get(name_or_power, creatures["goblin"])
        return random.choice(list(creatures.values()))

    def create_spell(self, name_or_power: str |
                     int | None = None) -> SpellCard:
        spells = {
            "fireball": SpellCard("Fireball", 4, "Uncommon", "damage"),
        }
        if isinstance(name_or_power, str):
            return spells.get(name_or_power, spells["fireball"])
        return spells["fireball"]

    def create_artifact(self, name_or_power: str | int |
                        None = None) -> ArtifactCard:
        artifacts = {
            "mana_ring": ArtifactCard(
                "Mana Ring",
                3,
                "Rare",
                4,
                "Permanent: +1 mana per turn"),
        }
        if isinstance(name_or_power, str):
            return artifacts.get(name_or_power, artifacts["mana_ring"])
        return artifacts["mana_ring"]

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            deck.append(self.create_creature())
        return {"deck": deck, "size": size, "theme": "Fantasy"}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
