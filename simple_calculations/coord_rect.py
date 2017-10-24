x1=float(input("X1:"))
y1=float(input("Y1:"))
x2=float(input("X2:"))
y2=float(input("Y2:"))

if x1<0:
    if x2<0:
        a= abs(x2-x1)
    else:
        a = abs(x2)+abs(x1)
if x1>0:
    if x2<0:
        a=abs(x1)+abs(x2)
    else:
        a=abs(x2-x1)
if y1<0:
    if y2<0:
        b= abs(y2-y1)
    else:
       b = abs(y2)+abs(y1)
if y1>0:
    if y2<0:
        b=abs(y1)+abs(y2)
    else:
        b=abs(y2-y1)

print(a*b)
print(2*a+2*b)

