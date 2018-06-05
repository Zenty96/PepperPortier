# -*- coding: utf-8 -*-
class Wegbeschreibung(object):
    def __getStockwerk(self, raumnummer):
        # Der Anfang der Raumnummer gibt das Stockwerk an
        ersterBuchstabe = raumnummer[:1]
        wegbeschreibung = ""

        if (ersterBuchstabe == 'U'):
            # U = Untergeschoss
            wegbeschreibung = "Gehen Sie über die Treppe einen Stock nach unten."
        elif (ersterBuchstabe == '0'):
            # 0 = Erdgeschoss
            wegbeschreibung = "Bleiben Sie auf diesem Stockwerk."
        elif (ersterBuchstabe == '1'):
            # 1 = Obergeschoss
            wegbeschreibung = "Gehen Sie über die Treppe einen Stock nach oben."
        elif (ersterBuchstabe == '2'):
            # 2 = Dachgeschoss
            wegbeschreibung = "Gehen Sie über die Treppe nach ganz oben."
        elif (ersterBuchstabe == 'M'):
            # M = Motorenprüfstand
            wegbeschreibung = "Gehen Sie zum Motorenprüfstand. Dieser befindet sich links hinter der Hochschule."

        return wegbeschreibung


    def __getWeg(self, raumnummer):
        # Nummer 2 und 3 geben den Raum an
        # 01 bis 10 rechts
        # 16 bis 23 geradeaus hinter
        # 30 bis 35 links
        nummer = int(raumnummer[1:3])
        wegbeschreibung = ""

        if (01 <= nummer <= 10):
            wegbeschreibung = "Gehen Sie dann den Gang nach rechts."
        elif (16 <= nummer <= 23):
            wegbeschreibung = "Gehen Sie dann den Gang gerade aus."
        elif (30 <= nummer <= 42):
            wegbeschreibung = "Gehen Sie dann den Gang nach links."

        return wegbeschreibung


    def __getGangseite(self, raumnummer):
        # A la "Der Raum befindet sich auf der rechten/linken Seite"
        pass


    def getWegbeschreibung(self, raumnummer):

        ersterBuchstabe = raumnummer[:1]
        erlaubteZeichen = {'M', 'U', '0', '1', '2'}

        # Falls ein unbekannter Raum genannt wird
        if (ersterBuchstabe not in erlaubteZeichen):
            return ""

        wegbeschreibung = self.__getStockwerk(raumnummer)

        if (raumnummer[:1] == 'M'):
            # keine weiteren Informationen zum Motorenprüfstand
            return wegbeschreibung
        else:
            # "..." für Sprechpause
            wegbeschreibung = wegbeschreibung + "..." + self.__getWeg(raumnummer)

        return wegbeschreibung

class Begruessung(object):
    def getBegruessung(self):
        # "..." für Sprechpause
        str = "Hallo..."
        str = str + "Ich bin Pepper und helfe Ihnen, sich hier zurecht zu finden..."
        str = str + "Fragen Sie mich nach einer Person oder Raumnummer und ich sage Ihnen den Weg."
        return str

class Verabschiedung(object):
    def getVerabschiedung(self):
        str = "Auf Wiedersehen."
        return str
