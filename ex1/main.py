# from ex0.Card import Card
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    print()
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Rare", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(
        ArtifactCard(
            "Mana Crystal",
            4,
            "Uncommon",
            5,
            "Permanent: +1 mana per turn"))
    print("Deck stats: ", deck.get_deck_stats())
    print()
    print("Drawing and playing cards:")
    print()
    for _ in range(3):
        card = deck.draw_card()
        print("Drew:", card.name,
              f"({type(card).__name__.replace('Card', '')})")
        print("Play result: ", card.play({}))
        print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
