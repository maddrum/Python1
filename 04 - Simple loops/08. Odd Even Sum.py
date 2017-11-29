n=int(input())
nOddSum=0
nEvenSum=0
for i in range(1,n+1):
    if i%2==0:
        nEven = int(input())
        nEvenSum = nEven + nEvenSum
    else:
        nOdd=int(input())
        nOddSum=nOdd+nOddSum
if nOddSum==nEvenSum:
    print("Yes \nSum = {}".format(nEvenSum))
else:
    print("No \nDiff = {}".format(abs(nEvenSum-nOddSum)))

