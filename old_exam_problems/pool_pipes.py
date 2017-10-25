v=int(input())
p1=int(input())
p2=int(input())
h=float(input())
h=round(h,2)
p1Flow=p1*he
p2Flow=p2*h
totalFLow=p1Flow+p2Flow
if v>=totalFLow:
    x=int(totalFLow/v*100)
    y=int(p1Flow/totalFLow*100)
    z=int(p2Flow/totalFLow*100)
    result="The pool is {}% full. Pipe 1: {}%. Pipe 2: {}%.".format(x,y,z)
    print(result)
else:
    overfill=totalFLow-v
    overfill="{0:.1f}".format(overfill)
    result = "For {} hours the pool overflows with {} liters.".format(h,overfill)
    print(result)