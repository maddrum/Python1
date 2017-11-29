n=int(input())
check = []
for i in range(1,10):
    if n%i == 0:
        check.append(i)
number=len(check)
if number ==1 and n !=1:
    exit()
for k in check:
    a=k
    for r in check:
        b=r
        for t in check:
            c=t
            for y in check:
                d=y
                for u in check:
                    e=u
                    for o in check:
                        f=o
                        if(a*b*c*d*e*f)==n:
                            print(str(a)+str(b)+str(c)+str(d)+str(e)+str(f),end=" ")

