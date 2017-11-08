n=int(input())
nLSum=0
nRSum=0
for i in range(0,n):
    nL = int(input())
    nLSum=nL+nLSum
for i in range (0,n):
    nR=int(input())
    nRSum=nR+nRSum
if nLSum==nRSum:
    print("Yes, sum = {}".format(abs(nLSum)))
else:
    print("No, diff = {}".format(abs(nLSum - nRSum)))
