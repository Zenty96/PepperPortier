# -*- coding: utf-8 -*-
import csv, sys
import Klassen
import Hilfsmittel
import time
import qi

class CSVReader(object):
    def __init__(self):
        pass

    def readCSV(self):
        filename = 'Ressourcen/Raumliste.csv'
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            try:
                liste = []
                for row in reader:
                    liste += row
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
            return liste

class ListenOperationen(object):
    def __init__(self):
        pass

    def getListeRauminformationen(self, liste):
        listeRauminformationen = []
        for info in liste:
            # String splitten
            nummer, zweck, personen = info.split(';')

            listeZwecke = []
            listeZwecke += zweck.split('&')

            listePersonen = []
            listePersonen += personen.split('&')

            # Werte zuweisen
            elementRaumInfos = Klassen.RaumInformationen(nummer, listeZwecke, listePersonen)

            # Elemente in Liste speichern
            listeRauminformationen.append(elementRaumInfos)

        return listeRauminformationen

    def getRaumnummerZuPerson(self, person):
        csvreader = Hilfsmittel.CSVReader()
        liste = csvreader.readCSV()
        listeRaumInfos = self.getListeRauminformationen(liste)

        rNum = 0

        for raum in listeRaumInfos:
            personenListe = raum.getPersonen()
            for p in personenListe:
                if (person in p):
                    rNum = raum.getRaumNummer()
                    return rNum

        return rNum

class PDF(object):
    def __init__(self):
        session = qi.Session()
        self.__tabletService = session.service("ALTabletService")

    def __getTabeltService(self):
        return self.__tabletService

    def anzeigen(self, raumnummer):
        tblService = __getTabeltService()
        # TODO korrekter Pfad
        pfadImage = raumnummer + ".pdf"
        tblService.loadUrl(pfadImage)
        tblService.showImageNoCache(pfadImage)

    def verstecken(self):
        time.sleep(10)
        tblService = __getTabeltService()
        tblService.hideImage()
