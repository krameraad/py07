from typing import Any

from tools.card_generator import CardGenerator
from . import Deck, CreatureCard, ArtifactCard, SpellCard


X = "\033[0m"
D = "\033[2m"
H = "\033[1m"

gen = CardGenerator()

game_state: dict[str, str | dict] = {
    "active_player": "Alice",
    "players": {
        "Alice": {
            "mana": 6,
            "field": [],
            "deck": Deck()
        },
        "Bob": {
            "mana": 3,
            "field": [],
            "deck": Deck()
        }
    }
}

print(f"{H}=== DataDeck Deck Builder ==={X}")
print(f"{D}Building deck with different card types...{X}")


def populate_deck(deck: Deck):
    for _ in range(3):
        deck.add_card(CreatureCard(**gen.get_random_creature()))
    for _ in range(3):
        deck.add_card(SpellCard(**gen.get_random_spell()))
    for _ in range(3):
        deck.add_card(ArtifactCard(**gen.get_random_artifact()))
    deck.shuffle()


deck_a: Deck = game_state["players"]["Alice"]["deck"]
deck_b: Deck = game_state["players"]["Bob"]["deck"]

populate_deck(deck_a)
populate_deck(deck_b)

print(deck_a.get_deck_stats())
print(f"{D}\nDrawing and playing cards...{X}")
for _ in range(5):
    card = deck_a.draw_card()
    print("Drew:", card.name, f"({card.__class__.__name__.removesuffix("Card")})")
    try:
        result = card.play(game_state)
        print("Play result:", result)
    except RuntimeError as e:
        print(e)
    print()

print(f"{H}\nPolymorphism: same interface, different card behaviors!{X}")
