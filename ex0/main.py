from tools.card_generator import CardGenerator
from .CreatureCard import CreatureCard


X = "\033[0m"
D = "\033[2m"
H = "\033[1m"

gen = CardGenerator()
dragon = CreatureCard(**gen.get_creature("Fire Dragon"))
goblin = CreatureCard(**gen.get_creature("Goblin Warrior"))

game_state: dict[str, str | dict] = {
    "active_player": "Alice",
    "players": {
        "Alice": {
            "mana": 6,
            "field": []
        },
        "Bob": {
            "mana": 3,
            "field": [goblin]
        }
    }
}

alice: dict = game_state["players"]["Alice"]
bob: dict = game_state["players"]["Bob"]

print(f"{H}=== DataDeck Card Foundation ==={X}")
print("Testing abstract base class design...")

print(f"{D}\nCreatureCard info...{X}")
print(dragon.get_card_info())
print(f"{D}\nPlaying {dragon.name}"
      f" with {alice["mana"]} mana available...{X}")
print("Playable:", dragon.is_playable(alice["mana"]))
print("Play result:", dragon.play(game_state))

print(f"{D}\n{dragon.name} attacks {goblin.name}...{X}")
print("Attack result:", dragon.attack_target(
    game_state["players"]["Bob"]["field"][0]))

print(f"{D}\nTesting insufficient mana"
      f" ({alice["mana"]} available)...{X}")
print("Playable:", dragon.is_playable(alice["mana"]))

print(f"{H}\nAbstract pattern successfully demonstrated!{X}")
