age=int(input())
priceW=float(input())
P=float(input())
check=age//2
sumM=0
if age%2!=0:
    sumP=P*(age//2+1)
else:
    sumP=P*(age//2)
for i in range(1,check+1):
    sumM=sumM+i*10-1
sum=sumM+sumP
if priceW<=sum:
    print("Yes! "+"{0:.2f}".format(sum-priceW))
else:
    print("No! " + "{0:.2f}".format(priceW-sum))

