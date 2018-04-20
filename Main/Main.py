# -*- coding: utf-8 -*-
from RaumInformationen import RaumInformationen

def main():
    var = RaumInformationen('U01', 'Vorlesung', 'Herr Herden')
    rNum = var.getRaumNummer()
    rPer = var.getPersonen()
    rZweck = var.getRaumZweck()

    print('Im Raum mit der Nummer %s sitzt %s, weil %s.') % (rNum, rPer, rZweck)

main()
