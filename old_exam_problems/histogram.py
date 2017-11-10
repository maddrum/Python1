n=int(input())
inputNumbers=[]
p1=0
p2=0
p3=0
p4=0
p5=0

for i in range(0,n):
    inputNumbers.append(int(input()))
for i in range(0,n):
    if inputNumbers[i]<200:
        p1=p1+1
    elif inputNumbers[i]>=200 and inputNumbers[i]<400:
        p2=p2+1
    elif inputNumbers[i]>=400 and inputNumbers[i]<600:
        p3=p3+1
    elif inputNumbers[i]>=600 and inputNumbers[i]<800:
        p4=p4+1
    else:
        p5=p5+1

print(p1+p2+p3+p4+p5)
print(n)
print("{0:.2f}".format(p1/n*100))
print("{0:.2f}".format(p2/n*100))
print("{0:.2f}".format(p3/n*100))
print("{0:.2f}".format(p4/n*100))
print("{0:.2f}".format(p5/n*100))

