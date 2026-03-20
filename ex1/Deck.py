import random

from . import Card, CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        index = -1
        for i, x in enumerate(self.cards):
            if x.name == card_name:
                index = i
                break
        if index != -1:
            self.cards.pop(index)
            return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        creatures = [x for x in self.cards if isinstance(x, CreatureCard)]
        spells = [x for x in self.cards if isinstance(x, SpellCard)]
        artifacts = [x for x in self.cards if isinstance(x, ArtifactCard)]
        try:
            avg_cost = sum([x.cost for x in self.cards]) / len(self.cards)
        except ZeroDivisionError:
            avg_cost = 0

        result = {
            "total_cards": len(self.cards),
            "creatures": len(creatures),
            "spells": len(spells),
            "artifacts": len(artifacts),
            "avg_cost": avg_cost,
        }
        return result
