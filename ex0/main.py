from tools.card_generator import CardGenerator
from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    X = "\033[0m"
    D = "\033[2m"
    H = "\033[1m"

    game_state = {"mana": 6}

    gen = CardGenerator()
    info = gen.get_creature("Fire Dragon")
    dragon = CreatureCard(*[v for k, v in info.items()])
    info = gen.get_creature("Goblin Warrior")
    goblin = CreatureCard(*[v for k, v in info.items()])

    print(f"{H}=== DataDeck Card Foundation ==={X}")
    print("Testing abstract base class design...")
    print(f"{D}\nCreatureCard info...{X}")
    print(dragon.get_card_info())
    print(f"{D}\nPlaying {dragon.name}"
          f" with {game_state["mana"]} mana available...{X}")
    print("Playable:", dragon.is_playable(game_state["mana"]))
    print("Play result:", dragon.play(game_state))
    print(f"{D}\n{dragon.name} attacks {goblin.name}...{X}")
    print("Attack result:", dragon.attack_target(goblin))
    print(f"{D}\nTesting insufficient mana"
          f" ({game_state["mana"]} available)...{X}")
    print("Playable:", dragon.is_playable(game_state["mana"]))
    print(f"{H}\nAbstract pattern successfully demonstrated!{X}")
