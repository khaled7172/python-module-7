*This project has been created as part of the 42 curriculum by khhammou*

# DataDeck - Master the Art of Abstract Card Architecture
## Description

DataDeck is a modular trading card game engine built in Python. It demonstrates abstract programming patterns including abstract base classes, multiple inheritance, interface composition, and design patterns such as Strategy and Abstract Factory.

## Structure

- **ex0** - Card Foundation: Abstract base class `Card` and concrete `CreatureCard`
- **ex1** - Deck Builder: `SpellCard`, `ArtifactCard`, and `Deck` management system
- **ex2** - Ability System: `Combatable` and `Magical` interfaces with `EliteCard` using multiple inheritance
- **ex3** - Game Engine: Strategy and Abstract Factory patterns with `GameEngine`, `AggressiveStrategy`, and `FantasyCardFactory`
- **ex4** - Tournament Platform: Full interface composition with `TournamentCard`, `Rankable`, and `TournamentPlatform`

## Usage

Run each exercise from the repository root:

```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
```

## Requirements

- Python 3.10 or later
- No external libraries required


### Instructions

You run this code by doing python3 -m exN.main

## Resources

The internet

## AI Usage

Testing my code with test cases and helping me find syntax errors