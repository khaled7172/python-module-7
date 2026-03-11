from ex2.EliteCard import EliteCard


def main() -> None:
    print()
    print("=== DataDeck Ability System ===")
    print()
    card = EliteCard("Arcane Warrior", 6, "Legendary", 5, 10, 4, 3)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()
    print(f"Playing {card.name} (Elite Card):")
    print()
    print("Combat phase:")
    print("Attack result:", card.attack("Enemy"))
    print("Defense result:", card.defend(5))
    print()
    print("Magic phase:")
    print("Spell cast:", card.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", card.channel_mana(3))
    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
