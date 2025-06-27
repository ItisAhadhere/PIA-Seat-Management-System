
import math
from random import *

COUNT = 5000

file = open("isidata.txt", "w+")

def GenRandID(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


file.write("%d\n" % (COUNT))
    
for i in range(COUNT):
    randomID = GenRandID(7)
    
    k = randint(0, 10000)
    if k < 100:
        status = "TERRORIST"
    else:
        status = "CLEAN"
    file.write("%d\t\t%s\n" % (randomID, status))
    
file.close()
