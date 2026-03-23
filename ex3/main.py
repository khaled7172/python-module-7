from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine.configure_engine(factory, strategy)
    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    print("Available types:", factory.get_supported_types())
    print()
    print("Simulating aggressive turn...")
    print("Hand:", [f"{c.name} ({c.cost})" for c in engine.hand])
    result = engine.simulate_turn()
    print("Turn execution:")
    print("Strategy:", result["strategy"])
    print("Actions:", {k: v for k, v in result.items() if k != "strategy"})
    print()
    print("Game Report:")
    print(engine.get_engine_status())
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
