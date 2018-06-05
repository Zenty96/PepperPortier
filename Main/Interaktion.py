# -*- coding: utf-8 -*-
import Konstanten
import Strings
import time
import Hilfsmittel
from naoqi import ALProxy

class Begruessung(object):
    def __init__(self, session):
        self.__session = session

    def sageBegruessung(self):

        ri = Konstanten.RoboterInformationen()
        tts = ALProxy("ALTextToSpeech", ri.getIP(), ri.getPort())

        begr = Strings.Begruessung()
        begruessung = begr.getBegruessung()

        tts.say(begruessung)

class Verabschiedung(object):
    def __init__(self, session):
        self.__session = session

    def sageVerabschiedung(self):

        ri = Konstanten.RoboterInformationen()
        tts = ALProxy("ALTextToSpeech", ri.getIP(), ri.getPort())

        begr = Strings.Verabschiedung()
        begruessung = begr.getVerabschiedung()

        tts.say(begruessung)



class Antwort(object):
    def __init__(self, session):
        self.__session = session

    def sageWegbeschreibung(self, eingabe):

        print("Eingabe: " + eingabe)
        ri = Konstanten.RoboterInformationen()
        tts = ALProxy("ALTextToSpeech", ri.getIP(), ri.getPort())

        weg = ""

        if (self.__istName(eingabe)):
            # Name -> Raumnummer suchen, dann Weitergabe zur Wegbeschreibung
            var = Hilfsmittel.ListenOperationen()
            rNum = var.getRaumnummerZuPerson(eingabe)
            rNumString = var.formatiereRaumnummerZuString(rNum)

            ein = Eingabe()
            ganzerName = ein.getGanzenNamen(eingabe)
            if (ganzerName.strip() != ""):
                weg = weg + "Das Büro von " + ganzerName + " hat die Raumnummer " + rNumString + "..."
                print(weg)
        else:
            # Raumnummer -> Weitergabe
            rNum = eingabe
            weg = weg + "Sie suchen den Raum mit der Nummer " + rNum + " ..."

        beschreibung = Strings.Wegbeschreibung()
        weg = weg + beschreibung.getWegbeschreibung(rNum)

        if (weg.strip() != ""):
            bild = Hilfsmittel.Bild(self.__session)
            bild.anzeigen(rNum)
            # Täblet, damit es wie im Englischen klingt
            tts.say(weg + "...Auf meinem Täblet habe ich den Raum für Sie markiert.")
            bild.verstecken()
        else:
            tts.say("Tut mir leid, ich kenne den Weg nicht.")

    def __istName(self, eingabe):

        istName = True
        ziffern = ["0", "1", "2", "3", "4"] # jede Raumnummer besitzt mindestens eine dieser Ziffern

        for zif in ziffern:
            zifferInEingabe = zif in eingabe
            if (zifferInEingabe == True):
                return False

        return istName


class Eingabe(object):
    def __init__(self):
        pass

    def getNutzerInput(self, counter):

        ri = Konstanten.RoboterInformationen()
        asr = self.__setVokabular(ri, counter)
        asr.subscribe("Portier_Test")

        # in dieser Zeit wartet Pepper auf einen Namen
        zeit = Konstanten.Zuhoerzeit()
        time.sleep(zeit.getZuhoerzeit())

        alm = ALProxy("ALMemory", ri.getIP(), ri.getPort())
        value = alm.getData("WordRecognized")[0]

        asr.unsubscribe("Portier_Test")

        return value

    def __setVokabular(self, ri, counter):
        asr = ALProxy("ALSpeechRecognition", ri.getIP(), ri.getPort())
        asr.pause(True)
        asr.setLanguage("German")

        if (counter == 0):
            # nur einmal beim ersten Mal
            vocabulary = self.__getListeRaumnummern()
            vocabulary = vocabulary + self.__getListeNachnamen()
            vocabulary.append('Ende') # Schlüsselwort, um die Abfrage zu beenden
            asr.setVocabulary(vocabulary, False) # True: achtet nur auf die Wörter aus dem Vokabular

        asr.pause(False)
        return asr

    def __getListeRaumInfos(self):
        csvreader = Hilfsmittel.CSVReader()
        liste = csvreader.readCSV()

        # liste beinhaltet alle Informationen zum jeweiligen Raum
        listeRauminformationen = []
        var = Hilfsmittel.ListenOperationen()
        listeRauminformationen = var.getListeRauminformationen(liste)

        return listeRauminformationen

    def __getListeRaumnummern(self):
        listeRauminformationen = self.__getListeRaumInfos()

        listeRaumnummern = []
        for raum in listeRauminformationen:
            num = raum.getRaumNummer()
            listeRaumnummern.append(num)

        return listeRaumnummern

    def __getListeNachnamen(self):
        listeRauminformationen = self.__getListeRaumInfos()

        listeNamen = []
        for name in listeRauminformationen:
            personen = name.getPersonen() #Liste an Personen
            # nur die Nachnamen ins Vokabular, auf das Pepper hören soll
            for p in personen:
                bestandteile = p.split(' ')
                nachname = bestandteile[-1] # letztes Element in der Liste
                if (nachname.strip() != ""):
                    listeNamen.append(nachname)

        return listeNamen

    def getGanzenNamen(self, nachname):
        listeRauminformationen = self.__getListeRaumInfos()

        listeNamen = []
        for name in listeRauminformationen:
            personen = name.getPersonen() # Liste an Personen
            for p in personen:
                if (nachname in p):
                    return p
