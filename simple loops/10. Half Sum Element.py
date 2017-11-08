n=int(input())
numbers = []
sum=0
max=0
otherSum=0
checker=0
maxSum=0
for i in range(0,n):
    numbers.append(int(input()))
for i in numbers:
    if i > max:
        max=i
for i in range(0,len(numbers)):
    otherSum = 0
    for j in range(0,len(numbers)):
        if i!=j:
            otherSum = otherSum +int(numbers[j])
    if otherSum==int(numbers[i]):
        checker = 1
        print("Yes\nSum = {}".format(numbers[i]))
    if numbers[i]==max:
        maxSum=otherSum
if checker == 0:
    print("No\nDiff = {}".format(abs(maxSum-max)))

