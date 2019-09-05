import string
import random

upper, lower, digits, symbols = 0, 0, 0, 0


def randompassword():
    password = ''
    chars = string.printable
    chars = chars.replace('\n', string.digits)
    size = random.randint(10, 16)
    return password.join(random.choice(chars) for x in range(size))


password = randompassword()
print(f"Random password generated of length {len(password)}\n", password)
