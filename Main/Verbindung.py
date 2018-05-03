# -*- coding: utf-8 -*-
import qi
import Konstanten

class Verbindung(object):

    def __init__(self):
        pass

    def aufbauen(self, lang):
        ri = Konstanten.RoboterInformationen()
        session = qi.Session()

        try:
            session.connect("tcp://{}:{}".format(ri.getIP(), ri.getPort()))
            alDialog = session.service("ALDialog")
            alDialog.setLanguage(lang)
            return session
        except RuntimeError:
            print ("\nCan't connect to Naoqi at IP {} (port {}).".format(ri.getIP(), ri.getPort()))
            return False
