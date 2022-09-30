import unittest
from conversions import *

#from conversions_refactored import convert

class ConversionTest(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        #celsius = 0
        result = ConvertCelsiusToKelvin(0)
        expected = 273.15
        self.assertEqual(result, expected)

        result = ConvertCelsiusToKelvin(300)
        expected = 573.15
        self.assertEqual(result, expected)

    def test_ConvertCelsiusToFahrenheit(self):
        result = ConvertCelsiusToFahrenheit(0)
        expected = 32
        self.assertEqual(result, expected)

        result = ConvertCelsiusToFahrenheit(21)
        expected = 69.8
        self.assertEqual(result, expected)

    def test_ConvertFahrenheitToCelsius(self):
        result = ConvertFahrenheitToCelsius(32)
        expected = 0
        self.assertEqual(result, expected)

        result = ConvertFahrenheitToCelsius(40)
        expected = 4.444444
        self.assertAlmostEqual(result, expected, places=6)

    
    def test_ConvertFahrenheitToKelvin(self):
        result = ConvertFahrenheitToKelvin(32)
        expected = 273.15
        self.assertAlmostEqual(result, expected, places=2)

    def test_MilesToYards(self):
        result = MilesToyards(12)
        expected = 21120
        self.assertEqual(result, expected)

    def test_MilesToMeters(self):
        result = MilesToMeters(15)
        expected = 24140.16
        self.assertEqual(result, expected)

    def test_MetersToMiles(self):
        result = MetersToMiles(20)
        excpected = 0.012427423844746679
        self.assertAlmostEqual(result, excpected, places=18)


  
if __name__ == '__main__':
    unittest.main()
