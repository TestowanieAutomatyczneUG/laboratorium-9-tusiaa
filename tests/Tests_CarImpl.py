from src.CarImpl import *
from unittest.mock import *
from unittest import TestCase, main

class test_Car_Impl(TestCase):

    @patch.object(Car, 'needsFuel')
    def test_needsFuelWarningTrue(self, mock_method):
        #prepare mock
        mock_method.return_value = True
        #testing
        test_object = CarImpl()
        result = test_object.needsFuelWarning()
        self.assertEqual("Trzeba zatankować!", result, 'return value incorrect')

    @patch.object(Car, 'needsFuel')
    def test_needsFuelWarningFalse(self, mock_method):
        #prepare mock
        mock_method.return_value = False
        #testing
        test_object = CarImpl()
        result = test_object.needsFuelWarning()
        self.assertEqual("Nie potrzebuje paliwa", result, 'return value incorrect')

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperatureIsRight(self, mock_method):
        #prepare mock
        mock_method.return_value = 90
        #testing
        test_object = CarImpl()
        result = test_object.getEngineTemperature_IsRight()
        self.assertEqual(True, result, 'return value incorrect')

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperatureIsRightToHigh(self, mock_method):
        #prepare mock
        mock_method.return_value = 120
        #testing
        test_object = CarImpl()
        result = test_object.getEngineTemperature_IsRight()
        self.assertEqual(False, result, 'return value incorrect')

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperatureIsRightToLow(self, mock_method):
        #prepare mock
        mock_method.return_value = 60
        #testing
        test_object = CarImpl()
        result = test_object.getEngineTemperature_IsRight()
        self.assertEqual(False, result, 'return value incorrect')

    @patch.object(Car, 'driveTo')
    def test_driveToHowManySteps1(self, mock_method):
        #prepare mock
        mock_method.return_value = ["one"]
        #testing
        test_object = CarImpl()
        result = test_object.driveToHowManySteps("UG")
        self.assertEqual(1, result, 'return value incorrect')

    @patch.object(Car, 'driveTo')
    def test_driveToHowManySteps5(self, mock_method):
        #prepare mock
        mock_method.return_value = ["one", "two", "three", "four", "five"]
        #testing
        test_object = CarImpl()
        result = test_object.driveToHowManySteps("UG")
        self.assertEqual(5, result, 'return value incorrect')

    @patch.object(Car, 'driveTo')
    def test_driveToHowManySteps10(self, mock_method):
        #prepare mock
        mock_method.return_value = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        #testing
        test_object = CarImpl()
        result = test_object.driveToHowManySteps("UG")
        self.assertEqual(10, result, 'return value incorrect')


    

if __name__ == '__main__':
    main()