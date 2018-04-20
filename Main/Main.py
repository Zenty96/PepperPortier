# -*- coding: utf-8 -*-
import Klassen
import Hilfsmittel

def main():
    var = Klassen.RaumInformationen('U01', ['Vorlesung'], ['Herr Herden'])
    rNum = var.getRaumNummer()
    rPer = var.getPersonen()
    rZweck = var.getRaumZweck()

    print('Im Raum mit der Nummer %s sitzt %s, weil %s.') % (rNum, rPer, rZweck)

    csvreader = Hilfsmittel.CSVReader()
    liste = csvreader.readCSV()

    # liste beinhaltet alle Raumnummer mit Informationen
    # -> Liste an RaumInformationen erstellen


main()
