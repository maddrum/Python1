import math
n = int(input())
size = len(str(n))
sum=0
for i in range(size-1,-1,-1):
    j = n//math.pow(10,i)
    k=j*math.pow(10,i)
    sum+=j
    n-=k
print( "{:g}".format(sum))

