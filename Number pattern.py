n = int(input("Rows: "))
print("Triangle:")
for i in range(1, n+1):
    print("* " * i)
print("Inverted:")
for i in range(n, 0, -1):
    print("* " * i)
print("Pyramid:")
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)