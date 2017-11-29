n = int(input())
t1=0
t2=0
t3=0
t4=0
t5=0

for i in range(0,n):
    k=float(input())
    if k<22.5:
        t1+=1
    elif k<40.5:
        t2+=1
    elif k<58.5:
        t3+=1
    elif k<76.5:
        t4+=1
    else:
        t5+=1
print("{0:.2f}% poor marks".format(t1/n*100))
print("{0:.2f}% satisfactory marks".format(t2/n*100))
print("{0:.2f}% good marks".format(t3/n*100))
print("{0:.2f}% very good marks".format(t4/n*100))
print("{0:.2f}% excellent marks".format(t5/n*100))






