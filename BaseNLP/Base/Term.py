# -*- coding:utf-8 -*-


class Term():

    def __init__(self, value):
        self.__Value = value
        self.__POS = ""
        self.__Index = -1

    def getValue(self):
        return self.__Value

    def setValue(self, value):
        self.__Value = value

    def getPOS(self):
        return self.__POS

    def setPOS(self, POS):
        self.__POS = POS

    def getIndex(self):
        return self.__Index

    def setIndex(self, index):
        self.__Index = index