from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print(logo + "\n")

operations = {"+": add, "-": sub, "*": mul, "/": div}
control = "n"

while True:

    if control == "n":
        number1 = float(input("What's the first number?: "))
    else:
        number1 = result

    for key in operations:
        print(key)
    symbol = input("Pick the operation: ")
    number2 = float(input("What's the next number?: "))

    result = operations[symbol](number1, number2)

    print(f"{number1} {symbol} {number2} = {result}")

    control = input(f"Type 'yes' to continue calculating with {result} or type 'n' to start a new calculation.")