class Happy:
    def __init__(self):
        self.happy=[]
    def isHappy(self,num):
        cache = []
        if num == 1:
            return True
        while num != 1:
            num = sum(int(i) ** 2 for i in str(num))
            if num in cache:
                return False
            cache.append(num)
        return True

    def happyGen(self):
        for h in range(1, 1001):
            if self.isHappy(h): self.happy.append(h)

    def happyFile(self):
        self.happyGen()
        happy = open("happy.txt", 'w')
        for h in self.happy:
            happy.write(f"{h}\n")
        happy.close()
