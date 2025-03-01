def eval_calculator(input):
    return eval(input)

# cosnt e = n => eval(n)
e = lambda n : eval(n)

print(eval_calculator("(1+1)*3/2"))