v=int(input())
p1=int(input())
p2=int(input())
h=float(input())
h=round(h,2)
p1Flow=p1*h
p2Flow=p2*h
totalFLow=p1Flow+p2Flow
if v>= totalFLow:
    x = totalFLow/v*100//1
    y = p1Flow/totalFLow*100//1
    z = p2Flow/totalFLow*100//1
    print("The pool is "+"{0:.0f}".format(x)+"% full. Pipe 1: "+"{0:.0f}".format(y)+"%. Pipe 2: "+"{0:.0f}".format(z)+"%.")
else:
    overfill = totalFLow-v
    if h%1 != 0:
        print("For {} hours the pool overflows with ".format(h) +"{0:.1f}".format(overfill)+" liters.")
    else:
        h=h//1
        print("For "+"{0:.0f}".format(h)+" hours the pool overflows with " + "{0:.1f}".format(overfill) + " liters.")
