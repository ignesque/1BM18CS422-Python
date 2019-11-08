from Prime import *
from Happy import *
Happy().happyFile()
Prime().primeFile()
overlap = []
happy=open("happy.txt")
prime=open("prime.txt")
happylist=happy.read().split()
primelist=prime.read().split()
for h in happylist:
    for p in primelist:
        if h==p:
            overlap.append(h)
print("The overlapping values in happy numbers and prime numbers are ")
print(", ".join(overlap))
print("The count of overlapping values ranging from 1 to 1000 are",len(overlap))
