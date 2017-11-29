a = int(input())
b = int(input())
h = float(input())
price = float(input())
weight = float(input())
lenght = 2* (a + b)
cost = lenght * price
area = lenght * h
weightTotal = area * weight
print(lenght)
print("{0:.2f}".format(cost))
print("{0:.3f}".format(weightTotal))