from .Card import Card


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
            ):
        super().__init__(name, cost, rarity)
        self.attack = max(attack, 0)
        self.health = max(health, 1)

    def get_card_info(self):
        info = super().get_card_info()
        info.update({"attack": self.attack, "health": self.health})
        return info

    def play(self, game_state: dict) -> dict:
        effect = "Failed to summon creature"
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

    def attack_target(self, target: "CreatureCard") -> dict:
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
