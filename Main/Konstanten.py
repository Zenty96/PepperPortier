# -*- coding: utf-8 -*-
class RoboterInformationen(object):
    def __init__(self):
        self.__ip = '10.1.1.68'
        self.__port = 9559

    def getIP(self):
        return self.__ip

    def getPort(self):
        return self.__port

class Zuhoerzeit(object):
    def getZuhoerzeit(self):
        return 6
