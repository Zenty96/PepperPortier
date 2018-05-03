# -*- coding: utf-8 -*-
import Konstanten
import Strings
import time
import Hilfsmittel
from naoqi import ALProxy

class Antwort(object):
    def __init__(self):
        pass

    def sageWegbeschreibung(self, rNum):

        ri = Konstanten.RoboterInformationen()
        tts = ALProxy("ALTextToSpeech", ri.getIP(), ri.getPort())

        beschreibung = Strings.Wegbeschreibung()
        weg = beschreibung.getWegbeschreibung(rNum)

        if (weg.strip() != ""):
            # Täblet, damit es wie im Englischen klingt
            tts.say(weg + "...Auf meinem Täblet habe ich den Raum für Sie markiert.")
        else:
            tts.say("Tut mir leid, ich kenne den Weg nicht.")

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
            asr.setVocabulary(vocabulary, False) # True: achtet nur auf die Wörter auf dem Vokabular

        asr.pause(False)
        return asr

    def __getListeRaumnummern(self):
        csvreader = Hilfsmittel.CSVReader()
        liste = csvreader.readCSV()

        # liste beinhaltet alle Raumnummer mit Informationen
        listeRauminformationen = []
        var = Hilfsmittel.ListenOperationen()
        listeRauminformationen = var.getListeRauminformationen(liste)

        listeRaumnummern = ['Ende']
        for raum in listeRauminformationen:
            num = raum.getRaumNummer()
            listeRaumnummern.append(num)

        return listeRaumnummern
