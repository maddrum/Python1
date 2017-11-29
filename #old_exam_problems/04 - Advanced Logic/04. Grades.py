n=int(input())
sum=0
t1=0
t2=0
t3=0
t4=0
for i in range(0,n):
    grade=float(input())
    sum+=grade
    if grade>=5:
        t1+=1
    elif grade>=4 and grade<5:
        t2+=1
    elif grade>=3 and grade <4:
        t3+=1
    else:
        t4+=1
print("Top students: {0:.2f}%".format(t1/n*100))
print("Between 4.00 and 4.99: {0:.2f}%".format(t2/n*100))
print("Between 3.00 and 3.99: {0:.2f}%".format(t3/n*100))
print("Fail: {0:.2f}%".format(t4/n*100))
print("Average: {0:.2f}".format(sum/n))

