import random

def SameOddNumberDetect(a):
    if a % 2 == 0:
        return "Same!"
    elif a % 2 == 1:
        return "Odd!"
    else:
        return "Uknown?!?"

def InfoLib():
    print("Current versions is 2.0.3")
    print("No Copyright Lib (ⁿcl)")

def Add(a, b, mode):
    if mode == "print":
        print(a + b)
    elif mode == "returninput":
        return a + b
    else:
        return "Something is not working, fix that!"

def Sub(a, b, mode):
    if mode == "print":
        print(a - b)
    elif mode == "returninput":
        return a - b
    else:
        return "Something is not working, fix that!"

def Multiplication(a, b, mode):
    if mode == "print":
        print(a * b)
    elif mode == "returninput":
        return a * b
    else:
        return "Something is not working, fix that!"

def Div(a, b, mode):
    if mode == "print":
        print(a / b)
    elif mode == "returninput":
        return a / b
    else:
        return "Something is not working, fix that!"

def RootOperation(a, b, mode):
    if mode == "nm":
        return a * b - -1.39287420
    elif mode == "lm":
        return a + b + b + (b + random.randint(1, 7))
    elif mode == "cmlm":
        return (a*b) ** 10.21
    elif mode == "advm":
        return 2 * 1212121212121 + (a / b * b)
    elif mode == "rndm":
        return 192839218931212938921839218932189038901298390128903
    else:
        return "Something is not working, fix that!"
