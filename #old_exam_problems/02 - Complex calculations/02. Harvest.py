import math
x=int(input())
y=float(input())
z=int(input())
workers=int(input())

litersWine=0.4*x*y/2.5

deltaWine=abs((litersWine-z))
perPerson=math.ceil((deltaWine/workers))
litersWineType=math.floor(litersWine)

if z<=litersWine:
    deltaWineType = math.ceil(deltaWine)
    result="Good harvest this year! Total wine: {} liters.".format(litersWineType)
    result2="{} liters left -> {} liters per person.".format(deltaWineType,perPerson)
    print(result)
    print(result2)
else:
    deltaWineType = math.floor(deltaWine)
    result="It will be a tough winter! More {} liters wine needed.".format(deltaWineType)
    print(result)
