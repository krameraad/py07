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
        active_player = game_state["players"][game_state["active_player"]]
        mana = active_player["mana"]
        if not self.is_playable(mana):
            raise RuntimeError(
                self.name
                + " could not be played: insufficient mana "
                + f"({mana} available, {self.cost} required)")

        active_player["mana"] -= self.cost
        active_player["field"].append(self)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        self.durability -= 1
        return {"effect": self.effect}
