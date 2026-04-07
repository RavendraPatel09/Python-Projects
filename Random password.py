import random
password = ""
for i in range(6):
    password += str(random.randint(0,9))
print("Password:", password)