# locations.py
import inventar


# ACHTUNG: ganz unten muss für jede neue Location ein Eintrag in der Location Registry vorgenommen werden!

def start(game): # Der Start des Spiels, kein wirklicher Ort. Hier kann eine Vorgeschichte erzählt werden.
        print("Du wachst auf, als eine Krähe anfängt gegen deinen Zeh zu picken.")
        print("Die Sonne scheint steil von oben auf dich herab. Es scheint wohl um die Mittagszeit zu sein.")
        print("Du kannst dich an nichts erinnern. Was ist in der letzten Nacht passiert? Nur ein blaues Licht scheint dir als Erinnerung geblieben zu sein.")
        print("Als du in deine Tasche greifst, ziehst du einen Ausweis heraus.")
        game.player = input("Du siehst auf das Foto und erkennst dein Gesicht. Daneben steht dein Name: ")
        print(f"Du denkst dir nur 'Guten Morgen, {game.player}' und siehst dich weiter um.\n")
        ausweis = inventar.Item("Personalausweis", "Dein Personalausweis mit einem Foto.") # Erstellt den Gegenstand "Personalausweis" mit Beschreibung
        game.inventar_spieler.add_item(ausweis) # Fügt den erstellten Gegenstand dem Inventar des Spielers hinzu

        game.current_location = location_registry["location_wald"] # Der Wechsel vom Start des Spiels zum ersten Ort.
        print("Du bist in einem düsteren Wald. Hinter dir ist eine strahlende Ebene. Am Eingang zum Wald steht ein Oger.") # Der Text des ersten Ortes muss auch hier ausgegeben werden, da er sonst nicht angezeigt wird.


def location_ebene(game, verb=None, target=None, preposition=None, second_target=None):
    if verb is None:
        print("Du befindest dich in einer weiten Ebene. Vor dir ist ein Wald. Rechts neben dir ist eine Mauer mit einem Tor.")
    elif verb == "gehe" and target == "wald":
        game.current_location = location_registry["location_wald"]
    elif verb == "gehe" and target in ["tor", "mauer"]:
        game.current_location = location_registry["tor"]
    elif verb == "untersuche":
        print("Du kannst nichts außergewöhnliches entdecken.")
    else:
        print("Das hat keinen Effekt.")


def location_wald(game, verb=None, target=None, preposition=None, second_target=None):
    if verb is None:
        print("Du bist in einem düsteren Wald. Hinter dir ist eine strahlende Ebene. Am Eingang zum Wald steht ein Oger.")
    elif verb == "gehe" and target == "ebene":
        game.current_location = location_registry["location_ebene"]
    elif verb == "rede" and target == "oger" and game.inventar_spieler.has_item("Klack") and game.inventar_spieler.has_item("Geheimer Schlüssel"):
        print(f"{game.player}: Hallo Klack.")
        print(f"Klack: Hallo {game.player}.")
    elif verb == "rede" and target == "oger" and game.inventar_spieler.has_item("Klack"):
        print(f"{game.player}: Hallo Klack.")
        print(f"Klack: Hallo {game.player}, was kann ich für dich tun?")
        print("1. Nichts, vielen Dank.")
        print("2. Weißt du, wie man durch das große Tor kommt?")
        auswahl = input("Bitte die gewünschte Zahl eingeben: ")
        if auswahl == "1":
            print(f"{game.player}: Nichts, vielen Dank.")
            print("Klack: Ok, bis bald.")
        elif auswahl == "2":
            print(f"{game.player}: Weißt du, wie man durch das große Tor kommt?")
            print("Klack: „Natürlich. Hier, nimm diesen Schlüssel. Damit kannst du das Tor öffnen.“")
            geheimer_schlüssel = inventar.Item("Geheimer Schlüssel", "Klack sagte, dass du damit das Tor öffnen kannst.", visible=True)
            game.inventar_spieler.add_item(geheimer_schlüssel)
            print(f"{game.player}: Danke für deine Hilfe!")
        else:
            print("Eingabe nicht erkannt.\n")
    elif verb == "rede" and target == "oger":
        print(f"{game.player}: Hallo, mein Name ist {game.player}, wer bist du?")
        print("Oger: Mein Name ist Klack, was kann ich für dich tun?")
        klack = inventar.Item("Klack", "Der Spieler hat mit Klack gesprochen", visible=False)
        game.inventar_spieler.add_item(klack)
        print("1. Nichts, vielen Dank.")
        print("2. Weißt du, wie man durch das große Tor kommt?")
        auswahl = input("Bitte die gewünschte Zahl eingeben: ")
        if auswahl == "1":
            print(f"{game.player}: Nichts, vielen Dank.")
            print("Klack: Ok, bis bald.")
        elif auswahl == "2":
            print(f"{game.player}: Weißt du, wie man durch das große Tor kommt?")
            print("Klack: Natürlich. Hier, nimm diesen Schlüssel. Damit kannst du das Tor öffnen.")
            geheimer_schlüssel = inventar.Item("Geheimer Schlüssel", "Klack sagte, dass du damit das Tor öffnen kannst.", visible=True)
            game.inventar_spieler.add_item(geheimer_schlüssel)
            print(f"{game.player}: Danke für deine Hilfe!")
        else:
            print("Eingabe nicht erkannt.\n")
    elif verb == "untersuche" and target == "wald":
            print("Der Wald ist sehr dunkel.")
    elif verb == "untersuche" and target == "oger":
        print("Ein großer, grüner Oger, der unerwartet freundlich aussieht.")
    elif verb == "untersuche":
        print("Du kannst nichts außergewöhnliches entdecken.")
    else:
        print("Das hat keinen Effekt.")


def tor(game, verb=None, target=None, preposition=None, second_target=None):
    if verb is None and game.inventar_spieler.has_item("Geheimer Schlüssel"): # Hier wird kontrolliert, ob ein Spieler ein gewisses Item im Inventar hat, um weiter zukommen. hat der Spieler das Item im Inventar, so erhält er einen anderen Text und andere Auswahlmöglichkeiten. Wichtig: name des Gegenstandes muss der aktuelle Name sein, nicht der Name der Variablen.
        print("Mit deinem Schlüssel öffnest du die schwere Tür und kannst passieren. Vor dir liegt ein Wald. Hinter dir erstreckt sich eine Ebene.")
    elif verb == "gehe" and target == "wald" and game.inventar_spieler.has_item("Geheimer Schlüssel"): # Der andere Weg muss ebenfalls mit der Bedingung des Gegenastandes verknüpft sein.
        game.current_location = location_registry["location_wald"]
    elif verb is None:
        print("Du stehst vor einer großen, verschlossenen Tür. Hier geht es vorerst nicht weiter. Hinter dir liegt eine Ebene.")
    elif verb == "gehe" and target == "ebene":
        game.current_location = location_registry["location_ebene"]
    elif verb == "untersuche" and target == "tor":
            print("Ein großes, altes Tor. Es hat eine Öffnung für einen Schlüssel in der Mitte.")
    elif verb == "untersuche":
        print("Du kannst nichts außergewöhnliches entdecken.")
    else:
        print("Das hat keinen Effekt.")

# Für jede neue Location in locations.py muss hier ein Eintrag erstellt werden. locations.[Name der Locations Funktion]

location_registry = {
    "location_ebene": location_ebene,
    "location_wald": location_wald,
    "start": start,
    "tor": tor

}
