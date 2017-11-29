import math
n = int(input())
checker=0
if n <2:
    print("Not prime")
else:
    k=int(math.sqrt(n))
    for i in range(2,k+1):
        if n%i==0:
            checker=1
    if checker ==0:
        print("Prime")
    else:
        print("Not prime")