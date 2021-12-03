from src.Checker import *
from unittest.mock import *
from unittest import TestCase, main

class test_Car_Impl(TestCase):

    @patch.object(Environment, 'getTime')
    def test_remainderBefore17(self, mock_method):
        #prepare mock
        mock_method.return_value = datetime(2020, 8, 4, 12, 00, 00, 00)
        #testing
        test_object = Checker()
        test_object.remainder("file")
        result = test_object.wasPlayed
        self.assertEqual(False, result, 'return value incorrect')

    @patch.object(Environment, 'getTime')
    def test_remainderAfter17(self, mock_method):
        #prepare mock
        mock_method.return_value = datetime(2020, 8, 4, 18, 00, 00, 00)
        #testing
        test_object = Checker()
        test_object.remainder("file")
        result = test_object.wasPlayed
        self.assertEqual(True, result, 'return value incorrect')
