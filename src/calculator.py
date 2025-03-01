def calculator(num1, num2, operator):
    result = 0
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "/":
            result = num1 / num2
        case "*":
            result = num1 * num2

    print(f"{num1} {operator} {num2} = {result}")
    return result

print(calculator(1,1,"+"))
print(calculator(10,5,"-"))
print(calculator(12,3,"/"))
print(calculator(4,4,"*"))
print(calculator(10,7,"apalah"))
