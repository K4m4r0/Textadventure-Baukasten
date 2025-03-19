# main.py

from menu import menu  
import inventar
from savegame import save_game, load_game
from locations import location_registry


class Game:
    def __init__(self):
        # Menu-Funktion als Start-Punkt
        self.menu = menu

        # Setze die Startlocation auf das Menü
        self.current_location = self.menu

        # Der Spielername (wird später durch Eingabe geändert)
        self.player = "Bob"

        # Zugriff auf Locations über die Registry
        self.locations = location_registry

        # Initialisiere das Spieler-Inventar
        self.inventar_spieler = inventar.Inventory()

        # Setze die Startlocation
        self.current_location = self.menu

        # Testitem unsichtbares Item, wird direkt zu Spielbeginn in das Inventar des Spielers gelegt
        # unsichtbares_item = inventar.Item("Unsichtbares Item", "Ein Item, das niemand sehen sollte.", visible=False)
        # self.inventar_spieler.add_item(unsichtbares_item)

    def parse_input(self, user_input):
        words = user_input.lower().strip().split()

        if "inventar" in words and len(words) == 1:  # and len(words) == 1 verhindert die versehentliche Nutzung in anderen Befehlen, wie zB "untersuche hilfe" oder "gehe zu laden"
            return "inventar", None, None, None
        if "hilfe" in words and len(words) == 1:
            return "hilfe", None, None, None
        if "speichern" in words and len(words) == 1:
            return "speichern", None, None, None
        if "laden" in words and len(words) == 1:
            return "laden", None, None, None
        if "ende" in words and len(words) == 1:
            return "ende", None, None, None
        if "name" in words and len(words) == 1:
            return "name", None, None, None

        # für Befehle wie: "benutze [Objekt] mit [Ziel]"
        if len(words) == 4 and words[2] == "mit":
            verb = words[0]
            target = words[1]
            preposition = words[2]
            second_target = words[3]
            return verb, target, preposition, second_target

        # für normale Befehle: "[Verb] [Ziel]"
        if len(words) == 2:
            verb = words[0]
            target = words[1]
            return verb, target, None, None

        # für Befehle zur Bewegung: "gehe zu [Ort]"
        if len(words) == 3 and words[1] == "zu":
            verb = words[0]
            target = words[2]
            return verb, target, None, None

        # diverse Befehle mit zB benutze der/die/das/den [Objekt]
        if len(words) == 3 and words[1] in ["die", "der", "das", "den"]:
            verb = words[0]
            target = words[2]
            return verb, target, None, None
        
        # Dummy-Parser zum testen
        if len(words) == 3 and words[1] == "mit":
            verb = words[0]
            target = words[2]
            return verb, target, None, None

        return None, None, None, None

    def execute_command(self, verb, target, preposition, second_target):
        if verb == "hilfe":
            print("Dies sind einige gültige Befehle: 'gehe zu [Ort]', 'untersuche [Ziel]', 'benutze [Objekt] mit [Ziel]', 'benutze [Ziel]', 'nimm [Ziel]', 'rede mit [Ziel]', 'inventar', 'speichern', 'laden', 'ende'.")

        elif verb == "inventar":
            print(f"Dein Inventar enthält:\n {self.inventar_spieler}\n")

        elif verb == "name":
            print(f"Dein Name lautet:\n {self.player}\n")

        elif verb == "speichern":
            save_game("spielstand.json", self.current_location.__name__, self.inventar_spieler, self.player)

        elif verb == "laden":
            location, inventory, name = load_game("spielstand.json", self.locations)
            if location and inventory and name:
                self.current_location = location
                self.inventar_spieler = inventory
                self.player = name

        elif verb == "ende":
            while True:
                ende = input("Möchtest du das Spiel wirklich beenden? Nicht gespeicherter Fortschritt geht verloren. (j/n) ").strip().lower()
                if ende == "j":
                    print("Das Spiel wird beendet. Bis zum nächsten Mal!")
                    exit()  # Beendet das Programm
                elif ende == "n":
                    print("Das Spiel wird fortgesetzt.\n")
                    break
                else:
                    print("Eingabe nicht erkannt.\n")

        elif self.current_location:
            self.current_location(self, verb, target, preposition, second_target)

        else:
            print("Das hat keinen Effekt.")

    def play(self):
        last_location = None  # last_location verhindert die andauernde Ausgabe des "if verb is None:" Befehls in location.py
        while True:
            if self.current_location != last_location:
                self.current_location(self)
                last_location = self.current_location

            command = input("Was möchtest du tun? ")
            verb, target, preposition, second_target = self.parse_input(command)
            if verb is not None:
                self.execute_command(verb, target, preposition, second_target)
                # Variable wird beim Location-Wechsel zurückgesetzt
                if self.current_location != last_location:
                    last_location = None
            else:
                print("Ungültiger Befehl.")

if __name__ == "__main__":
    game = Game()
    game.play()
