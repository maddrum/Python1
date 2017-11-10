n=int(input())
numbers = []
sum=0
for i in range(0,n):
    numbers.append(input())
for i in range(0,n):
    sum =sum + int(numbers[i])
print(sum)