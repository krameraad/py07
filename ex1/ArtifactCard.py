from . import Card


class ArtifactCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        effect = "Failed to play"
        active_player = game_state["players"][game_state["active_player"]]

        if self.is_playable(active_player["mana"]):
            effect = "Creature summoned to battlefield"
            active_player["mana"] -= self.cost
            active_player["field"].append(self)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }

    def activate_ability(self) -> dict:
        pass
