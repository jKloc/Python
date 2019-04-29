def adding(x, y):
    return (int(x) + int(y))

def substracting(x, y):
    return (int(x) - int(y))

def multiplication(x, y):
    return (int(x) * int(y))

def dividing(x, y):
    return (int(x) / int(y))

def calc_func(argument, num1, num2):
    switcher = {
        1: adding,
        2: substracting,
        3: multiplication,
        4: dividing
    }
    # import pdb;pdb.set_trace()
    action = switcher.get(int(argument), None)
    if not action:
        return "You choose invalid option"
    result = action(num1, num2)
    return result