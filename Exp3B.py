import string
import random

def gen():
    data = string.ascii_letters+string.punctuation+string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(data) for x in range(size))


password = gen()
print(f"Random password generated of length {len(password)}\n",password)
