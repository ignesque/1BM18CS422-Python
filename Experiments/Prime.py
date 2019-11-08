class Prime:
    def __init__(self):
        self.prime = []

    def isPrime(self, num):
        if num == 2:
            return True
        for factor in range(2, num):
            if num % factor == 0:
                return False
        return True

    def primeGen(self):
        for p in range(2, 1000):
            if self.isPrime(p):
                self.prime.append(p)
        return self.prime

    def primeFile(self):
        self.primeGen()
        prime = open("prime.txt", 'w')
        for p in self.prime:
            prime.write(f"{p}\n")
        prime.close()
