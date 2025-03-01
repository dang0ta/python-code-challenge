import calculator;

def string_calculator(input):
    s = input.split()
    num1, operator, num2 = s[0], s[1], s[2]
    return calculator.calculator(int(num1), int(num2), operator)

string_calculator("1 + 1")