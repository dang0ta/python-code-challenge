def convert_temperature(value, unit):
    result = 0
    resultUnit = "c"
    if unit == "c":
        resultUnit = "f"
    if unit == "f":
        result =  (value - 32) * 5/9
    else:
        result =  (value * 9/5) + 32
    print(f"converted {value}{unit} is {result}{resultUnit}")
    return result
    

assert convert_temperature(0, "c") == 32
assert convert_temperature(100, "c") == 212
assert convert_temperature(32,"f") == 0
assert convert_temperature(212,"f") == 100