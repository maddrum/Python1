n=int(input())
nMax=0
for i in range(0,n):
    x1=int(input())
    x2=int(input())
    nSum = x1+x2
    if i==0:
        diff=0
        difMax=0
    elif lSum>=nSum:
        diff=lSum-nSum
    else:
        diff=nSum-lSum
    if diff>difMax:
        difMax=diff
    lSum=nSum

if difMax==0:
    print("Yes, value={}".format(nSum))
else:
    print("No, maxdiff={}".format(difMax))

