class RaumInformationen(object):
    def __init__(self, raumnummer, raumzweck, personen):
        self.__RaumNummer = raumnummer #ein Wert
        self.__RaumZweck = raumzweck # Liste an Werten
        self.__Personen = personen # Liste an Personennamen

    def getRaumNummer(self):
        return self.__RaumNummer

    def getRaumZweck(self):
        return self.__RaumZweck

    def getPersonen(self):
        return self.__Personen
