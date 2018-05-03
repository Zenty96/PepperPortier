# -*- coding: utf-8 -*-
import Klassen
import Hilfsmittel
import Verbindung
import Konstanten
import Strings
import Interaktion

def main():
    rNum = '345' # Test

    verb = Verbindung.Verbindung();
    session = verb.aufbauen("German")

    if (session == False):
        print("Fehler beim Aufbauen der Verbindung")
        exit() # Beenden

    weiter = True
    counter = 0
    while(weiter):
        # Input vom Benutzer
        eingabe = Interaktion.Eingabe()
        nutzerEingabe = eingabe.getNutzerInput(counter)
        # Counter, sodass das Setzen vom Vokabular nur einmal passiert
        counter = counter + 1

        print(nutzerEingabe)

        if (nutzerEingabe == "Beenden" or nutzerEingabe == "Ende"):
            # zum Beenden der Schleife
            weiter = False
            print("Ende angefragt")
            exit()

        # Nummer -> kein Problem, weitergeben
        # Name -> Nummer suchen, dann weitergeben

        # Antwort von Pepper
        antwort = Interaktion.Antwort()
        antwort.sageWegbeschreibung(nutzerEingabe)

        bild = Hilfsmittel.Bild()
        bild.anzeigen(nutzerEingabe)

main()
