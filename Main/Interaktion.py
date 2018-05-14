# -*- coding: utf-8 -*-
import Konstanten
import Strings
import time
import Hilfsmittel
from naoqi import ALProxy

class Antwort(object):
    def __init__(self):
        pass

    def sageWegbeschreibung(self, eingabe):

        ri = Konstanten.RoboterInformationen()
        tts = ALProxy("ALTextToSpeech", ri.getIP(), ri.getPort())

        weg = ""

        if (self.__istName(eingabe)):
            # Name -> Raumnummer suchen, dann Weitergabe zur Wegbeschreibung
            var = Hilfsmittel.ListenOperationen()
            rNum = var.getRaumnummerZuPerson(eingabe)
            print(rNum)

            # TODO
            weg = weg + "Das Büro von " + eingabe + "hat die Raumnummer " + rNum
        else:
            # Raumnummer -> Weitergabe
            rNum = eingabe

        beschreibung = Strings.Wegbeschreibung()
        weg = weg + beschreibung.getWegbeschreibung(rNum)

        if (weg.strip() != ""):
            # Täblet, damit es wie im Englischen klingt
            tts.say(weg + "...Auf meinem Täblet habe ich den Raum für Sie markiert.")
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
        time.sleep(7)

        alm = ALProxy("ALMemory", ri.getIP(), ri.getPort())
        value = alm.getData("WordRecognized")[0]

        asr.unsubscribe("Portier_Test")

        return value

    def __setVokabular(self, ri, counter):
        asr = ALProxy("ALSpeechRecognition", ri.getIP(), ri.getPort())
        asr.setLanguage("German")
        asr.pause(True)

        if (counter == 0):
            # nur einmal beim ersten Mal
            vocabulary = self.__getListeRaumnummern()
            vocabulary.append(self.__getListeNamen())
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

    def __getListeNamen(self):
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
