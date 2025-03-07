# menu.py

import savegame
from locations import location_registry


def menu(game, verb=None):
    print("             _                 _                   ")
    print("    /\      | |               | |                  ")
    print("   /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___  ")
    print("  / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ")
    print(" / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ ")
    print("/_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___| \n")
                                                  
    print("\n\nHerzlich willkommen. Was möchtest du tun?")
    print("1. Neues Spiel")
    print("2. Laden")
    print("3. Ende")
    auswahl = input("Bitte die gewünschte Zahl eingeben: ")
    if auswahl == "1":
        game.current_location = location_registry["start"] 
        game.current_location(game)  # Ruft die Startfunktion auf, um den Begrüßungstext anzuzeigen
    elif auswahl == "2":
        location, inventory, name = savegame.load_game("spielstand.json", location_registry)
        if location and inventory and name:
            game.current_location = location
            game.inventar_spieler = inventory
            game.player = name
            game.current_location(game)  # Zeigt den Text der geladenen Location an
    elif auswahl == "3":
        exit()
    else:
        print("Eingabe nicht erkannt.\n")
