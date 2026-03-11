from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.consumed = False
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        self.consumed = True
        effect = None
        if self.effect_type == "damage":
            effect = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            effect = "healed 3 points"
        elif self.effect_type == "buff":
            effect = "Gained 1 mana"
        elif self.effect_type == "debuff":
            effect = "Lost 1 mana"
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }
