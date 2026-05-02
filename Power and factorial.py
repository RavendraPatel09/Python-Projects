def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
while True:
    mode = input("factorial / power / quit: ")
    if mode == "factorial":
        n = int(input("Number: "))
        print(f"{n}! = {factorial(n)}")
    elif mode == "power":
        b = int(input("Base: "))
        e = int(input("Exponent: "))
        print(f"{b}^{e} = {power(b, e)}")
    elif mode == "quit":
        break
