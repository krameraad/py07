import random
from . import Card, CreatureCard, ArtifactCard, SpellCard


class Deck:
    def add_card(self, card: Card) -> None:
        try:
            self.cards.append(card)
        except AttributeError:
            self.cards: list[Card] = [card]

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
        avg_cost = sum([x.cost for x in self.cards]) / len(self.cards)

        result = {
            "total_cards": len(self.cards),
            "creatures": len(creatures),
            "spells": len(spells),
            "artifacts": len(artifacts),
            "avg_cost": avg_cost,
        }
        return result
