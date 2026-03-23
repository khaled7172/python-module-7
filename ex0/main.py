from ex0.CreatureCard import CreatureCard


def main() -> None:
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    print("CreatureCard Info:")
    c = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(c.get_card_info())
    print()
    mana = 6
    print(f"Playing Fire Dragon with {mana} mana available:")
    print("Playable: ", c.is_playable(6))
    print("Play result: ", c.play({}))  # maybe shouldnt send it empty idk
    print()
    print("Fire Dragon attacks Goblin Warrior:")
    print("Attack result: ", c.attack_target("Goblin Warrior"))
    print()
    print("Testing insufficient mana (3 available):")
    print("Playable: ", c.is_playable(3))
    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
