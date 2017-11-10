import math
year=input()
p=int(input())
h=int(input())


total = (48-h)*3/4+2/3*p+h

if year == "leap":
    total = total+.15*total

print(math.floor(total))
