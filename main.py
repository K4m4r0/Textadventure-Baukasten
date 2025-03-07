# main.py

from menu import menu  # Import der menu-Funktion aus der neuen Datei
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
        #unsichtbares_item = inventar.Item("Unsichtbares Item", "Ein Item, das niemand sehen sollte.", visible=False)
        #self.inventar_spieler.add_item(unsichtbares_item)

    def parse_input(self, user_input):
        words = user_input.lower().strip().split()

        if "inventar" in words:
            return "inventar", None, None
        if "hilfe" in words:
            return "hilfe", None, None
        if "speichern" in words:
            return "speichern", None, None
        if "laden" in words:
            return "laden", None, None
        if "ende" in words:
            return "ende", None, None
        if "name" in words:
            return "name", None, None

        if len(words) == 2:
            verb = words[0]
            target = words[1]
            return verb, target, None
        if len(words) == 3 and words[1] == "zu":
            verb = words[0]
            target = words[2]
            return verb, target, None
        if len(words) == 4 and words[2] == "mit":
            verb = words[0]
            target = words[1]
            preposition = "mit"
            second_target = words[3]
            return verb, target, f"{preposition} {second_target}"
        if len(words) == 3 and words[1] == "mit":
            verb = words[0]
            target = words[2]
            return verb, target, None

        return None, None, None

    def execute_command(self, verb, target, preposition):
        if verb == "hilfe":
            print("Dies sind einige gültige Befehle: 'gehe zu [Ort]', 'untersuche [Ziel]', 'benutze [Objekt] mit [Ziel]', 'rede mit [Ziel]', 'speichern', 'laden', 'ende'.")

        elif verb == "inventar":
            print(f"Dein Inventar enthält:\n {self.inventar_spieler}\n")

        elif verb == "name":
            print(f"Dein Name lautet:\n {self.player}\n")

        elif verb == "speichern":
            save_game("spielstand.json", self.current_location.__name__, self.inventar_spieler, self.player)

        elif verb == "laden":
           location, inventory, name = load_game("spielstand.json", location_registry)
           if location and inventory and name:
               game.current_location = location
               game.inventar_spieler = inventory
               game.player = name
               #game.current_location(game)

        elif verb == "ende":
            ende = input("Möchtest du das Spiel wirklich beenden? (j/n) ").strip().lower()
            if ende == "j":
                print("Das Spiel wird beendet. Bis zum nächsten Mal!")
                exit()  # Beendet das Programm
            elif ende == "n":
                print("Das Spiel wird fortgesetzt.\n")
            else:
                print("Eingabe nicht erkannt.\n")

        elif self.current_location:
            self.current_location(self, verb, target, preposition)

        else:
            print("Befehl nicht erkannt.")

    def play(self):
        while True:
            self.current_location(self)
            command = input("Was möchtest du tun? ")
            verb, target, preposition = self.parse_input(command)
            if verb is not None:
                self.execute_command(verb, target, preposition)
            else:
                print("Ungültiger Befehl.")

if __name__ == "__main__":
    game = Game()
    game.play()

