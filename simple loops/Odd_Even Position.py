n=int(input())
oddSum=0
oddMin=0
oddMax=0
evenSum=0
evenMax=0
evenMin=0
checkerEven=0
checkerOdd=0
if n == 0:
    print("OddSum=0,")
    print("OddMin=No,")
    print("OddMax=No,")
    print("EvenSum=0,")
    print("EvenMin=No,")
    print("EvenMax=No")
    exit()
if n==1:
    j = int(input())
    print("OddSum={},".format(j))
    print("OddMin={},".format(j))
    print("OddMax={},".format(j))
    print("EvenSum=0,")
    print("EvenMin=No,")
    print("EvenMax=No")
    exit()
for i in range(1,n+1):
    j=float(input())
    if i==1:
        oddMin=j
        oddMax=j
    if i==2:
        evenMin=j
        evenMax=j
    if i%2==0:
        evenSum=evenSum+j
        if evenMax<j:
            evenMax = j
        if evenMin>j:
            evenMin=j
    else:
        oddSum=oddSum+j
        if oddMax<j:
            oddMax=j
        if oddMin>j:
            oddMin=j
if oddSum-oddSum//1>0:
    print("OddSum={},".format(oddSum))
else:
    print("OddSum={},".format(round(oddSum)))
if oddMin-oddMin//1>0:
    print("OddMin={},".format(oddMin))
else:
    print("OddMin={},".format(round(oddMin)))
if oddMax-oddMax//1>0:
    print("OddMax={},".format(oddMax))
else:
    print("OddMax={},".format(round(oddMax)))

if evenSum-evenSum//1>0:
    print("evenSum={},".format(evenSum))
else:
    print("evenSum={},".format(round(evenSum)))
if evenMin-evenMin//1>0:
    print("evenMin={},".format(evenMin))
else:
    print("evenMin={},".format(round(evenMin)))
if evenMax-evenMax//1>0:
    print("evenMax={},".format(evenMax))
else:
    print("evenMax={},".format(round(evenMax)))



