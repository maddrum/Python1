x1 = int(input())
x2 = int(input())
while x2 != 0:
    c=x1
    x1 = x2
    x2 = c % x2
print(x1)