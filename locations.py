# locations.py
import inventar


# ACHTUNG: ganz unten muss für jede neue Location ein Eintrag in der Location Registry vorgenommen werden!

def start(game):
        print("Du wachst auf, als eine Krähe anfängt gegen deinen Zeh zu picken.")
        print("Die Sonne scheint steil von oben auf dich herab. Es scheint wohl um die Mittagszeit zu sein.")
        print("Du kannst dich an nichts erinnern. Was ist in der letzten Nacht passiert? Nur ein blaues Licht scheint dir als Erinnerung geblieben zu sein.")
        print("Als du in deine Tasche greifst, ziehst du einen Ausweis heraus.")
        print("Auf diesem Dokument liest du 'Vereinigte Europäische Föderation'. Neben dem Schriftzug prangt das Logo der New World Order.")
        game.player = input("Du siehst auf das Foto und erkennst dein Gesicht. Daneben steht dein Name: ")
        print(f"Du denkst dir nur 'Guten Morgen, {game.player}' und siehst dich weiter um.\n")
        ausweis = inventar.Item("Personalausweis", "Dein Personalausweis mit einem Foto.")
        game.inventar_spieler.add_item(ausweis)

        game.current_location = location_registry["location_wald"]
        print("Du bist in einem düsteren Wald. Hinter dir ist eine strahlende Ebene.")


def location_ebene(game, verb=None, target=None, preposition=None):
    if verb is None:
        print("Du befindest dich in einer weiten Ebene. Vor dir ist ein Wald. Rechts neben dir ist eine Mauer mit einem Tor.")
    elif verb == "gehe" and target == "wald":
        game.current_location = location_registry["location_wald"]
    elif verb == "gehe" and target == "tor":
        game.current_location = location_registry["tor"]
    else:
        print("Befehl nicht erkannt.")


def location_wald(game, verb=None, target=None, preposition=None):
    if verb is None:
        print("Du bist in einem düsteren Wald. Hinter dir ist eine strahlende Ebene.")
    elif verb == "gehe" and target == "ebene":
        game.current_location = location_registry["location_ebene"]
    elif verb == "untersuche":
            print("Der Wald ist sehr dunkel.")
    else:
        print("Befehl nicht erkannt.")


def tor(game, verb=None, target=None, preposition=None):
    if verb is None and game.inventar_spieler.has_item("Geheimer Schlüssel"): # Hier wird kontrolliert, ob ein Spieler ein gewisses Item im Inventar hat, um weiter zukommen. hat der Spieler das Item im Inventar, so erhält er einen anderen Text und andere Auswahlmöglichkeiten. Wichtig: name des Gegenstandes muss der aktuelle Name sein, nicht der Name der Variablen.
        print("Mit deinem Schlüssel öffnest du die schwere Tür und kannst passieren. Du siehst einen Wald. Hinter dir ist eine Ebene.")
    elif verb == "gehe" and target == "wald" and game.inventar_spieler.has_item("Geheimer Schlüssel"): # Der andere Weg muss ebenfalls mit der Bedingung des Gegenastandes verknüpft sein.
        game.current_location = location_registry["location_wald"]
    elif verb is None:
        print("Du stehst vor einer großen verschlossenen Tür. Hier geht es vorerst nicht weiter. Hinter dir ist eine Ebene.")
    elif verb == "gehe" and target == "ebene":
        game.current_location = location_registry["location_ebene"]
    elif verb == "untersuche":
            print("Der Wald ist sehr dunkel.")
    else:
        print("Befehl nicht erkannt.")

# Für jede neue Location in locations.py muss hier ein Eintrag erstellt werden. locations.[Name der Locations Funktion]

location_registry = {
    "location_ebene": location_ebene,
    "location_wald": location_wald,
    "start": start,
    "tor": tor

}
