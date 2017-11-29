n=int(input())
g1=0
g2=0
g3=0
g4=0
g5=0
sum=0
for i in range(0,n):
    j=int(input())
    sum+=j
    if j<=5:
        g1+=j
    elif j<=12:
        g2+=j
    elif j<=25:
        g3+=j
    elif j<=40:
        g4+=j
    else:
        g5+=j
print("{0:.2f}%".format(g1/sum*100))
print("{0:.2f}%".format(g2/sum*100))
print("{0:.2f}%".format(g3/sum*100))
print("{0:.2f}%".format(g4/sum*100))
print("{0:.2f}%".format(g5/sum*100))
