from src.environment import *

class Checker:
    def __init__(self):
        self.environment = Environment()
        self.wasPlayed = False

    def remainder(self, file):
        self.resetWav()
        if self.environment.getTime().hour >= 17:
            self.environment.playWavFile(file)
            self.wavWasPlayed()

    def wavWasPlayed(self):
        self.wasPlayed = True

    def resetWav(self):
        self.wasPlayed = False