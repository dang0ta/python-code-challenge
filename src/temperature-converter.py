class InvalidUnitException(Exception):
    def __init__(self):
        super().__init__("Invalid conversion unit, the conversion unit should be either 'f' or 'c'")

class InvalidConversionValue(Exception):
    def __init__(self):
        super().__init__("Invalid conversion value, the value should be either numeric string, int, or float")

def validate_conversion(value, unit):
    unit = unit.lower()
    if not isinstance(value, (int, float, str)):
        raise InvalidConversionValue()
    if isinstance(value, str) and not value.isdigit():
        raise InvalidConversionValue()
    if unit not in ['f', 'c']:
        raise InvalidUnitException()
    return unit

def convert_temperature(value, unit):
    unit = validate_conversion(value, unit)
    
    conversion = {
        "f": lambda value: (value - 32) * 5/9,
        "c": lambda value: (value * 9/5) + 32
    }

    return conversion[unit](float(value))

if __name__ == "__main__":
    assert convert_temperature(0, "c") == 32
    assert convert_temperature(100, "c") == 212
    assert convert_temperature(32,"f") == 0
    assert convert_temperature(212,"f") == 100

    assert convert_temperature('0', "c") == 32
    assert convert_temperature('100', "c") == 212
    assert convert_temperature('32',"f") == 0
    assert convert_temperature('212',"f") == 100

    assert convert_temperature(0, "C") == 32
    assert convert_temperature(100, "C") == 212
    assert convert_temperature(32,"F") == 0
    assert convert_temperature(212,"F") == 100

    assert convert_temperature('0', "C") == 32
    assert convert_temperature('100', "C") == 212
    assert convert_temperature('32',"F") == 0
    assert convert_temperature('212',"F") == 100

    try:
        convert_temperature(0, "x") == 32
    except InvalidUnitException:
        print("invalid value properly captured")

    try:
        convert_temperature({}, "c") == 32
    except InvalidConversionValue:
        print("invalid value properly captured")

    try:
        convert_temperature("abcd", "c") == 32
    except InvalidConversionValue:
        print("invalid value properly captured")

    try:
        convert_temperature((), "c") == 32
    except InvalidConversionValue:
        print("invalid value properly captured")

    try:
        convert_temperature([], "c") == 32
    except InvalidConversionValue:
        print("invalid value properly captured")