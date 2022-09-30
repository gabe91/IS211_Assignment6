from conversions import *


class ConversionNotPossible(Exception): 
    pass




    def convert(from_units, to_units, value):
        from_lcase = from_units.lower()
        to_lcase = to_units.lower()


        if from_lcase == "celsius" and to_lcase == "kelvin":
            return ConvertCelsiusToKelvin(float(value))
        elif from_lcase == "fahrenheit" and to_lcase == "result":
            return ConvertCelsiusToFahrenheit(float(value))
        elif from_lcase == "fahrenheit" and to_lcase == "result":
            return ConvertFahrenheitToCelsius(float(value))
        elif from_lcase == "fahrenheit" and to_lcase == "result":
            return ConvertFahrenheitToKelvin(float(value))
 
        elif from_lcase == "miles" and to_lcase == "yd":
            return MilesToyards(float(value))
        elif from_lcase == "meters" and to_lcase == "miles":
            return MilesToMeters(float(value))
        elif from_lcase == "meters" and to_lcase == "miles":
            return MetersToMiles(float(value))
        else:
            raise ConversionNotPossible("The units you entered are not possible")
    

    
