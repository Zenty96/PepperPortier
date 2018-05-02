# -*- coding: utf-8 -*-
import Klassen
import Hilfsmittel
import Verbindung
import Konstanten
from naoqi import ALProxy

def main():
    var = Klassen.RaumInformationen('U01', ['Vorlesung'], ['Herr Herden'])
    rNum = var.getRaumNummer()
    rPer = var.getPersonen()
    rZweck = var.getRaumZweck()

    print('Im Raum mit der Nummer %s sitzt %s, weil %s.') % (rNum, rPer, rZweck)

    csvreader = Hilfsmittel.CSVReader()
    liste = csvreader.readCSV()

    # liste beinhaltet alle Raumnummer mit Informationen
    listeRauminformationen = []
    var = Hilfsmittel.ListenOperationen()
    listeRauminformationen = var.getListeRauminformationen(liste)

    # Test, ob alles da ist (108 Räume)
    #print len(listeRauminformationen)

    verb = Verbindung.Verbindung();
    if(verb.aufbauen()):
        print('Verbindung aufgebaut')

    # mit Pepper testen
    #ri = Konstanten.RoboterInformationen()
    #tts = ALProxy("ALTextToSpeech", ri.getIP(), ri.getPort())
    #tts.say("Hello, world!")

    #Topic-File einbinden (Verbindung zu Pepper (da muss es hochgeladen sein) oder hier eintippen (eigene Datei in Ressourcen))

    # Bild anzeigen (muss auf Pepper hochgeladen sein)


main()
