from src.Car import *

class CarImpl():
    def __init__(self):
        self.car = Car()

    def needsFuelWarning(self):
        if self.car.needsFuel():
            return "Trzeba zatankować!"
        else:
            return "Nie potrzebuje paliwa"

    def getEngineTemperature_IsRight(self):
        if self.car.getEngineTemperature() < 100 and self.car.getEngineTemperature() > 80:
            return True
        else:
            return False

    def driveToHowManySteps(self, destination):
        return len(self.car.driveTo(destination))