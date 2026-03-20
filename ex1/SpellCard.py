from . import Card, CreatureCard


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        active_player = game_state["players"][game_state["active_player"]]
        mana = active_player["mana"]
        if not self.is_playable(mana):
            raise RuntimeError(
                self.name
                + " could not be played: insufficient mana "
                + f"({mana} available, {self.cost} required)")

        active_player["mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        if self.effect_type == "damage":
            for x in targets:
                if isinstance(x, CreatureCard):
                    x.health -= self.cost
                    return {"effect": f"Dealt {self.cost} damage to {x.name}"}
        elif self.effect_type == "heal":
            for x in targets:
                if isinstance(x, CreatureCard):
                    x.health += self.cost
                    return {"effect": f"Healed {self.cost} health to {x.name}"}
        elif self.effect_type == "debuff" or self.effect_type == "buff":
            for x in targets:
                if isinstance(x, CreatureCard):
                    return {
                        "effect":
                        f"Applied {self.effect_type} {self.name} to {x.name}"}
        raise ValueError(f"{self.effect_type} is not a valid effect type.")
