
class UnitsNotExisting(Exception): pass



def ConvertCelsiusToKelvin(celsius):
    kelvin = celsius + 273.15

    return kelvin


def ConvertCelsiusToFahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32

    return fahrenheit

def ConvertFahrenheitToCelsius(fahrenheit):
    result = (fahrenheit - 32) * 5/9

    return result

def ConvertFahrenheitToKelvin(fahrenheit):
    result = (fahrenheit - 32) * 5/9 + 273.15

    return result



def MilesToyards(miles):
    yd = miles * 1760

    return yd

def MilesToMeters(meters):
    miles = meters * 1609.344

    return miles

def MetersToMiles(meters):
    miles = meters / 1609.344

    return miles


