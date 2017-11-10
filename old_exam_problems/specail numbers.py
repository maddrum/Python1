n=int(input())
numbers=[]
for i in range(1,10):
    if n%i ==0:
        numbers.append(i)
for i in numbers:
    a=i
    for j in numbers:
        b=j
        for k in numbers:
            c=k
            for l in numbers:
                d=l
                print(str(a)+str(b)+str(c)+str(d),end=" ")
