import math
kg = float(input())
x = int(input())
y = int(input())
total = kg / 5
b1 = total / 0.535
kasNum = b1 / y
total1=math.floor(total)
print("Total lutenica: {} kilograms.".format(total1))
if x > kasNum:
    diff = x - kasNum
    print("{} more boxes needed.".format(math.floor(diff)))
    print("{} more jars needed.".format(math.floor(diff*y)))
else:
    diff = kasNum-x
    print("{} boxes left.".format(math.floor(diff)))
    print("{} jars left.".format(math.floor(diff * y)))


