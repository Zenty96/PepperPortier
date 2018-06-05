# -*- coding: utf-8 -*-
import Klassen
import Hilfsmittel
import Verbindung
import Konstanten
import Strings
import Interaktion
import time

def main():

    verb = Verbindung.Verbindung();
    session = verb.aufbauen("German")

    if (session == False):
        print("Fehler beim Aufbauen der Verbindung")
        exit() # Beenden

    begruessung = Interaktion.Begruessung(session)
    begruessung.sageBegruessung()

    weiter = True
    counter = 0

    while(weiter):

        # Input vom Benutzer
        eingabe = Interaktion.Eingabe()
        nutzerEingabe = eingabe.getNutzerInput(counter)
        # Counter, sodass das Setzen vom Vokabular nur einmal passiert
        counter = counter + 1

        if (nutzerEingabe == "Beenden" or nutzerEingabe == "Ende"):
            # zum Beenden der Schleife
            weiter = False
            print("Ende angefragt")
            verabschiedung = Interaktion.Verabschiedung(session)
            verabschiedung.sageVerabschiedung()
            exit()

        # Antwort von Pepper
        antwort = Interaktion.Antwort(session)
        antwort.sageWegbeschreibung(nutzerEingabe)


main()
