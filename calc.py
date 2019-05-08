def adding(x, y):
    return (int(x) + int(y))

def substracting(x, y):
    return (int(x) - int(y))

def multiplication(x, y):
    return (int(x) * int(y))

def dividing(x, y):
    if y != 0:
        return (int(x) / int(y))
    else:
        print("second value must be different than 0")

def percents(x):
    return (int(x)/100)

def factorial(x):
    if x > 1:
        return x * factorial(x - 1)
    elif x in (0, 1):
        return 1
    elif x < 0:
        print("value must be higher than 0")
    else:
        print("value must be integer")

def exponentiation(x, y):
    if y >= 1 or y <= 0:
        return x ** y
    elif y == 0:
        return 1
    else:
        print("This is only exponentiation function. If you want to root choose this option")

def square_rooting(x, y):
    return x**(1./y)

def calc_func(argument, num1, num2=None):
    switcher = {
        1: adding,
        2: substracting,
        3: multiplication,
        4: dividing,
        5: percents,
        6: factorial,
        7: exponentiation,
        8: square_rooting
    }
    # import pdb;pdb.set_trace()
    action = switcher.get(argument, None)
    if not action:
        return "You choose invalid option"
    if argument in (5, 6):
       result = action(num1)
    else:
        result = action(num1, num2)
    return result