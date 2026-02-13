import json
from pathlib import Path

script_dir = Path(__file__).resolve().parent
json_path = script_dir / "pokemon.json"

try:
    with json_path.open("r", encoding="utf-8") as file:
        pokemons = json.load(file)
        if not isinstance(pokemons, list):
            print("Warning: pokemon.json does not contain a list. Starting empty list.")
            pokemons = []
except FileNotFoundError:
    print(f"{json_path.name} not found — starting with empty list.")
    pokemons = []
except json.JSONDecodeError:
    print(f"{json_path.name} is not valid JSON — starting with empty list.")
    pokemons = []

print("Current pokemons in file:", pokemons)

name = input("Pokemon Name:")
type_ = input("Pokemon Type:")

while True:
    level_raw = input("Pokemon Level:")
    try:
        level = int(level_raw)
        break
    except ValueError:
        print("Please enter a valid integer for the level.")
    
hp = int(input("HP: "))
attack = int(input("Attack: "))
defense = int(input("Defense: "))
sp_attack = int(input("Sp. Attack: "))
sp_defense = int(input("Sp. Defense: "))
speed = int(input("Speed: "))

new_pokemon = {
    "name": name,
    "type": type_,
    "level": level,
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}



print("New pokemon (not saved yet):", new_pokemon)

updated_pokemons = pokemons + [new_pokemon]

print("updated list (about to be saved):", updated_pokemons)

with json_path.open("w", encoding="utf-8") as file:
    json.dump(updated_pokemons, file, indent=4, ensure_ascii=False)

print("Pokemon saved.")
