from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print()
    print("=== DataDeck Tournament Platform ===")
    print()
    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, "dragon_001")
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 3, 4, "wizard_001")

    platform.register_card(dragon)
    platform.register_card(wizard)
    wizard.rating = 1150

    print("Registering Tournament Cards...")
    print()
    for card in [dragon, wizard]:
        print(f"{card.name} (ID: {card.card_id}):")
        print("  - Interfaces: [Card, Combatable, Rankable]")
        print(f"  - Rating: {card.rating}")
        print(f"  - Record: {card.wins}-{card.losses}")
        print()

    print("Creating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)
    print()

    print("Tournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - Rating: {entry['rating']}"
            f"({entry['record']})"
            )
    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
