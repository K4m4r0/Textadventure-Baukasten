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
    print("\n")
    while True:
        print("\nHerzlich willkommen bei Adventure. Was möchtest du tun?")
        print("1. Neues Spiel")
        print("2. Laden")
        print("3. Optionen")
        print("4. Ende")
        auswahl = input("Bitte die gewünschte Zahl eingeben: ")
        if auswahl == "1":
            game.current_location = location_registry["start"]  # Zugriff über die Location-Registry
            game.current_location(game)  # Ruft die Startfunktion auf, um den Begrüßungstext anzuzeigen
            break
        elif auswahl == "2":
            location, inventory, name = savegame.load_game("spielstand.json", location_registry)
            if location and inventory and name:
                game.current_location = location
                game.inventar_spieler = inventory
                game.player = name
                game.current_location(game)  # Zeigt den Text der geladenen Location an
                break
            else:
                print("Spielstand konnte nicht geladen werden.")
        elif auswahl == "3":
            print("Optionen:")
            print("Das Spiel wir durch Eingabe von Befehlen gesteuert.")
            print("Dies sind die gültigen Befehle: \n"
                  "'gehe zu [Ort]' - Bewege dich zum gewünschten Ort\n"
                  "'untersuche [Ziel]' - Untersuche das gewünschte Ziel\n"
                  "'benutze [Objekt] mit [Ziel]' - Benutze ein Objekt mit einem Ziel\n"
                  "'benutze [Ziel]' - Benutze das gewünschte Ziel\n"
                  "'nimm [Ziel]' - Nimm das gewünschte Ziel\n"
                  "'rede mit [Ziel]' - Rede mit dem gewünschten Ziel\n"
                  "'inventar' - Zeigt die Gegenstände in deinem Inventar an\n"
                  "'speichern' - Speichert das Spiel\n"
                  "'laden' - Lädt einen vorherigen Spielstand\n"
                  "'ende' - Beendet das Spiel\n"
                  "'hilfe' - Zeigt die Befehle im Spiel an\n\n"
                  "Für jedes [Ziel], [Objekt] und jeden [Ort] ist immer nur ein Wort einzugeben.")
        elif auswahl == "4":
            exit()
        else:
            print("Eingabe nicht erkannt.\n")

