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

print("OddSum={:g},".format(oddSum))
print("OddMin={:g},".format(oddMin))
print("OddMax={:g},".format(oddMax))
print("evenSum={:g},".format(evenSum))
print("evenMin={:g},".format(evenMin))
print("evenMax={:g}".format(evenMax))


