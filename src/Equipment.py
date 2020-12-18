#!/usr/bin/env python3

class Equipment:

    def __init__(self, name, type, data, flags, effects, img):

        self.name = name
        self.type = type
        self.data = data
        self.flags = flags
        self.effects = effects
        self.img = img

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getData(self):
        return self.data

    def getFlags(self):
        return self.flags

    def getEffects(self):
        return self.effects

    def getImg(self):
        return self.img

    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setData(self, data):
        self.data = data

    def setFlags(self, flags):
        self.flags = flags

    def setEffects(self, effects):
        self.effects = effects

    def setImg(self, img):
        self.img = img
