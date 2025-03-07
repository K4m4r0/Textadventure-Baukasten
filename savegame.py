# savegame.py

import json
from inventar import Inventory


def save_game(filename, current_location_key, inventory, player):
    state = {
        "current_location": current_location_key,
        "inventar_spieler": inventory.to_dict(),
        "name-spieler": player
    }
    try:
        with open(filename, 'w') as file:
            json.dump(state, file)
        print(f"Spielstand wurde in {filename} gespeichert.")
    except IOError:
        print("Fehler: Spielstand konnte nicht gespeichert werden.")


def load_game(filename, locations):
    try:
        with open(filename, 'r') as file:
            state = json.load(file)
            location_key = state["current_location"]
            current_location = locations.get(location_key, None)
            inventar_spieler = Inventory.from_dict(state["inventar_spieler"], suppress_output=True)
            name = state["name-spieler"]
            print(f"Spielstand von {filename} geladen.")
            return current_location, inventar_spieler, name
    except (IOError, ValueError) as e:
        print(f"Fehler: Spielstand konnte nicht geladen werden. {e}")
        return None, None
