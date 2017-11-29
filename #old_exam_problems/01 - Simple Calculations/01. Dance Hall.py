import math
l=float(input())
w=float(input())
a=float(input())
area=l*100*w*100
areaWard=a*100*a*100
areaBench=area/10
freeSpace=area-areaBench-areaWard
dancers=math.floor(freeSpace/7040)
print(dancers)

