v=float(input())
t1=float(input())
t2=float(input())
t3=float(input())
t1=t1/60
t2=t2/60
t3=t3/60
sum = t1*v
v=1.10*v
sum += t2 * v
v = 0.95 * v
sum += v * t3
print("{0:.2f}".format(sum))
