# get all factors of n
import math
n=12
factors=set()
for i in range(1,int(math.sqrt(n))):
    if n % i == 0:
        factors.add(i)
        factors.add(n//i)
print(factors)