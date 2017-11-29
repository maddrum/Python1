import math
def square():
    b=float(input())
    area = b*b
    return area;
def rectangle():
    a=float(input())
    b=float(input())
    area = a*b
    return area;
def circle():
    r = float(input())
    area = math.pi*r*r
    return area
def triangle():
    a=float(input())
    h=float(input())
    area = a*h/2
    return area;

type=input()
if type =="square":
    area=round(square(),3)
    print(area)
elif type =="rectangle":
    area=round(rectangle(),3)
    print(area)
elif type =="circle":
    area=round(circle(),3)
    print(area)
elif type == "triangle":
    area=round(triangle(),3)
    print(area)
else:
    print("error!")

