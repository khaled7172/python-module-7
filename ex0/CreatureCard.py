from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("attack must be positive")
        self.attack = attack
        if health <= 0:
            raise ValueError("health must be positive")
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        }
